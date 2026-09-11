##### C.4.7.4. Strong completion, law continuity and reached uniqueness

The preceding source argument supplies a radius \(\rho>0\), a mesh
threshold and constants \(a,M>0\) such that all sufficiently fine
finite-law raw Euler programs in \(U_\rho\) satisfy
\[
 \tau_R(c_k)+\int\tau_R(Q_k(u))\,d\mu(u,y)
                      \le M e^{-aR}\quad(R\ge1).
 \tag{NH}
\]
It actually supplies Gaussian tails for every passive query. The weaker
exponential estimate (NH) is enough for the remaining construction.
All constants are uniform on a fixed smaller neighborhood. Choose
\(0<\delta_Y<\rho/4\); further decreases do not affect the argument.

For two Euler interpolants on meshes of maximal steps \(h,h'\), with
laws \(\mu,\nu\) in that smaller neighborhood, put
\[
 s(t)=d(\theta^h_\mu(t),\theta^{h'}_\nu(t))
                     +q+V_T(h+h'),\qquad q=\mathcal W_1(\mu,\nu).
\]
The preceding-node distance is at most the current distance plus
\(V_T(h+h')\). Apply (NC) at these nodes and (NH), and choose
\(R=1+a^{-1}\log(1/s)\). For \(0<s\le1\) this gives almost everywhere
\[
 s'(t)\le Ls(t)\log(e/s(t)),\qquad
 s(t)\le e^{1-\alpha(t)}s(0)^{\alpha(t)},\quad
                         \alpha(t)=e^{-Lt}>0.
 \tag{NO}
\]
To verify the integration, set \(z=\log(e/s)\); then \(z'\ge-Lz\).
Multiplication by \(e^{Lt}\) and integration prove the displayed bound.
At a zero value use \(s+\eta\), the monotonicity of
\(v\log(e/v)\) on \((0,1)\), and then \(\eta\downarrow0\).
For sufficiently small initial s the bound remains below one through T,
so a first-exit argument validates its use on the whole interval. For
larger errors the common raw bound (NE) suffices. No lower bound on the
tail exponent relative to T is needed.

Finite probability laws are dense in \(\mathcal W_1\) on the compact
data domain: partition it into finitely many Borel cells of diameter at
most b, move each cell's mass to a representative, and pay at most b.
For any \(\mu\in U_Y\), take such finite laws \(\nu_j\to\mu\) and
meshes \(h_j\to0\). They eventually lie in a fixed smaller neighborhood
where (NH) is uniform. Formula (NO) makes the Euler paths Cauchy in
\(C([0,T];\mathcal E)\), including the HS component. The same estimate
between any two families makes the limit independent of both choices.
Their preceding-node states have the same limit. Joint field continuity
proved after (NC) now passes their integral equations to
\[
 \theta_\mu(t)=(g,0,0)+\int_0^t\mathcal F_\mu(\theta_\mu(s))\,ds.
 \tag{NI}
\]
The convergence of the integrands is uniform in time. Otherwise a sequence
of discrepant times has a convergent subsequence, and joint continuity at
the corresponding limiting state and law gives a contradiction. Thus
(NI) is a strong \(C^1\) equation in all three raw components, and every
coefficient is computed from the current state and the fixed law. Its
energy and readout bounds are (NG).

The needed tails pass to the constructed paths without a coordinate
supremum assumption. For fixed R the map
\(v\mapsto(|v|-R)_+\) is 1-Lipschitz on \(L^2\), and
\[
 \|v\mathbf1_{|v|>2R}\|_2
                \le2\|(|v|-R)_+\|_2\le2\tau_R(v).
 \tag{NP}
\]
Uniform state convergence and bounded multiplier continuity imply
uniform-in-input Q convergence at a fixed time. The resulting continuous
positive-part norms pass also through the converging law integral.
Consequently (NH), with an enlarged M and exponent \(a/2\), holds for
the constructed path, at every time with the same constants.

Comparing two such paths by (NC), their tails and (NO) proves (NL), with
\(a_Y=e^{-LT}\) after changing constants. The forward formulas give
\[
 \sup_u\|H^{(1)}_\theta(u)-H^{(1)}_{\bar\theta}(u)\|_2
          \le\|w-\bar w\|_2,
\]
\[
 \sup_u\|Z^{(2)}_\theta(u)-Z^{(2)}_{\bar\theta}(u)\|_2
          \le\|A\|_{\rm op}\|w-\bar w\|_2+\|K-\bar K\|_{\rm HS}.
\]
Together with bounded c these give the same type of uniform prediction
modulus. Common raw bounds give its constant large-q branch.

An arbitrary competing strong raw solution on the prescribed carrier
has a bounded path on a compact interval. Apply (NC) with that competitor
as its first endpoint and the constructed solution as its tail-bearing
second endpoint. Only the latter's tails enter. Formula (NO) at zero
initial discrepancy proves equality. Applying this argument on
\([s,40]\) proves the reached-state uniqueness and restart assertion.
Existence for this restart is furnished by the restriction of (NI);
neither new Gaussian roots nor a local theorem from every ambient state
is needed. No extra tail or weighted regularity is imposed on a
competitor.

We will also need the law comparison on one common Euler mesh with no
mesh-error floor. Subtract the two recursions at the same node and use
(NC) and (NH). If \(s_k=d(\theta^h_\mu(t_k),\theta^h_\nu(t_k))+q\),
then
\(s_{k+1}\le s_k+L\Delta_k s_k\log(e/s_k)\) below one. Compare each
step with the scalar increasing solution of
\(v'=Lv\log(e/v)\): its derivative increases while \(v<1\), so its
exact increment dominates the Euler increment. Induction and the same
first-exit bound give
\[
 \sup_k d(\theta^h_\mu(t_k),\theta^h_\nu(t_k))
                      \le Cq^{a_Y}.
 \tag{NLM}
\]
All constants remain uniform on the smaller neighborhood. Bounded c and
the displayed forward inequalities also give
\(\sup_u\|Q_\theta(u)-Q_{\bar\theta}(u)\|_2\le C d(\theta,\bar\theta)\)
for these Euler states: subtract \(A^*\Delta^{(2)}\) and use the
uniform pointwise bound on the comparison readout in its gate product.

##### C.4.7.5. Actual finite GF and the observation limits

The population tail estimate does not by itself assert a finite-width
moment theorem. We therefore give the approximation order explicitly.
Fix one finite comparison law \(\nu\) in the neighborhood and one fine
raw Euler mesh h. The resulting population program has finitely many
instructions. Expand K as its finite sum of ranks, and realize this
program on the actual initialized finite arrays using its deterministic
population residuals and contractions. Include the actual finite initial
readout additively in the proxy parameters, as in C.4.3 (A3). Its assigned
increments are the oracle increments. Actual GF and proxy therefore start
at the same finite arrays.

The complete fixed-program theorem III.F.1–7 and A.1 applies to this
fixed graph. Its roots are the two first-row Gaussians, the two queried
orientations are \(A_0\) and its actual adjoint, and the coordinate
instructions are continuous of at most linear growth. A backward product
is a bounded gate times a named \(L^2\) field. To recover the recomputed
proxy feedback from the oracle instructions, subtract each gate product,
truncate its fixed oracle field as in (NT), take width to infinity and
remove that cutoff using its joint second-moment limit. Scalar
contractions converge by the two-factor RMS inequality. The finite rank
expansion handles learned actions in both orientations. The finite
initial readout RMS and supremum tend to zero; the same finite induction
propagates this additive discrepancy while preserving the actual finite
initialization.

At this fixed \((\nu,h)\), recomputed proxy fields and assigned
velocities consequently differ from their oracle versions by
\(o_{\mathbb P}(1)\). The proxy lies on a deterministic enlargement
of the ball (NE) with probability tending to one. Its increment norm and
pairings have exactly their HS interpretation: if
\(K=\sum_i a_i\otimes b_i\) and
\(\widetilde K=\sum_j\tilde a_j\otimes\tilde b_j\), then
\[
 \langle K,\widetilde K\rangle_{\rm HS}
       =\sum_{i,j}\langle a_i,\tilde a_j\rangle
                    \langle b_i,\tilde b_j\rangle.
 \tag{NK}
\]
The finite Frobenius contraction of ranks \(a_ib_i^T/n\) is the same
sum of normalized pairings. Each is an identified same-layer second
moment, so (NK) involves no cross-carrier subtraction.

For any fixed cutoff R, positive-part second-moment convergence, (NP)
and (NH) imply at the finitely many proxy nodes
\[
 \tau_R(\bar c_n(t_k))+
       \int\tau_R(\bar Q_n(t_k,u))\,d\nu
                         \le M'e^{-a'R}+o_{\mathbb P}(1).
 \tag{NPT}
\]
These are normalized finite RMS tails. The constants \(M',a'>0\) are
independent of the chosen law and mesh in the smaller neighborhood;
fixed cutoff rescaling changes only these constants. No growing
transcript has been submitted to a fixed-program theorem.

Let \(\lambda_j\to\mu\) in \(\mathcal W_1\), with
\(n_j\to\infty\). The actual laws may here be arbitrary Borel laws;
only the proxy law is finite. Compare actual GF with the proxy on their
common finite carrier, using the law-independent finite energy bounds
and (NC). A proxy interpolant differs from its preceding node by at most
\(V'h+o_{\mathbb P}(1)\). On any interval \([b_0,b_1]\) of length
at most \(\ell\), the sum distance E obeys
\[
 \sup_{b_0\le t\le b_1}E(t)
 \le e^{C(1+R)\ell}E(b_0)
   +C\ell e^{C(1+R)\ell}
    \{(1+R)(\mathcal W_1(\lambda_j,\nu)+h)
                     +M'e^{-a'R}+o_{\mathbb P}(1)\}.
 \tag{NAP}
\]
The proxy velocity defect is included in the fixed-program probability
error. Every random error here is for fixed \(\nu,h,R\).

Choose a finite time partition with \(C\ell<a'/2\). On each interval
the amplified tail in (NAP) tends to zero as R increases. For a required
final accuracy, choose the last interval's cutoff and its required
incoming accuracy, then the preceding interval's cutoff and incoming
accuracy, and continue backwards over the finite partition. This produces
finitely many fixed cutoffs and positive tolerances. Next choose the
finite law \(\nu\) close enough to \(\mu\), and h small enough, so
all their deterministic errors meet these tolerances. Finally take
\(j\to\infty\). The finitely many fixed-program probability errors
and \(\mathcal W_1(\lambda_j,\mu)\) vanish together. Forward induction
in (NAP) gives arbitrarily small finite GF/proxy raw error through40.
This choice order is why an arbitrarily small positive tail exponent
suffices. It neither asserts a finite moment bound uniform over all laws
nor requires a relation between sample count and width.

The population proxy converges in raw norm to (NI), while each fixed
proxy's joint node laws, action tests, and pairings converge by the
fixed-program theorem. These two comparisons prove the stated state
identification. Forward/prediction formulas are Lipschitz on the bounded
raw balls, uniformly in u. Full row bounds give input continuity, and
the velocity bound gives the needed time continuity. Finite time/input
nets, with the fixed-program limit at their nodes, yield (NW2).
Holding \(\lambda_j=\mu\) for all j in precisely the same comparison
proves (NW1), including for a nonatomic Borel law with exact loss
integration. No empirical total-variation approximation has been used.

Here are the further observation passages. In any same-carrier
comparison, applying a named bounded action costs its norm times the
input error, plus the input norm times the HS increment error if the
learned action changes. A globally Lipschitz coordinate operation
preserves \(L^2\) approximation. For a fixed bounded continuous gate
times a named \(L^2\) field, first truncate that field and restrict the
gate arguments to a compact box. On the box uniform continuity applies;
off it the joint second-moment limits give tightness and uniform
integrability. Remove the restrictions after the fixed approximation
limit. Induction over a finite observation program proves the joint
same-layer \(\mathcal W_2\) limit and all quadratic contractions in
the theorem. Keeping the initialized and current hidden fields in the
same tuple gives the paired observations. This argument admits no
arbitrary unbounded product and makes no operator-norm comparison
between carriers.

For iid data of size m, the compact partition proof is elementary.
Move both \(\mu\) and its empirical law to the representatives of a
partition with cell diameter b. The two moves cost at most \(2b\).
The remaining distance is at most half the data diameter times the sum
of cell-mass discrepancies. Each empirical cell frequency has variance
at most \(1/(4m)\), so this remaining term tends to zero in probability
for the fixed finite partition. First let m increase, then b decrease.
Thus empirical \(\mathcal W_1\) converges in probability. All proxy
events in (NAP) concern its fixed law and initialization, independent of
the observations. Combining these events and the data-distance event
by a finite union bound proves the iid conclusion for arbitrary
\(m_j,n_j\to\infty\).
