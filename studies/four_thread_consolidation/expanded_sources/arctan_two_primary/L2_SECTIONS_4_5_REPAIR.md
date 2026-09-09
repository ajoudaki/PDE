# Insertion-ready repairs for Sections 4 and 5

## Replacement for the oracle-coupling paragraph in Section 4

The bars in (4.3) describe a finite-dimensional tensor-program oracle with population coefficients; they are not, at finite \(n\), the exact Euler variables of a learned matrix.  To compare the oracle to the Euler network without conflating these two objects, define its finite-width rank memory by
\[
 \bar{B}_{k}^{(n)}
 :=B_0-2\delta\sum_{r<k}\bar e_r\bar D_r\otimes_n\bar H_r .       \tag{4.4}
\]
(Here and below the decoration on \(\bar B_k^{(n)}\) is only a bar; it is written separately from the oracle probes to emphasize that (4.3), rather than multiplication by this finite matrix, defines \(\bar S_k,\bar P_k\).)  Put
\[
 \widehat a_{rk}^{(n)}=\langle\bar H_r,\bar H_k\rangle_n,
 \quad a_{rk}=\mathbb E[\bar H_r\bar H_k],
 \qquad
 \widehat b_{rk}^{(n)}=\langle\bar D_r,\bar D_k\rangle_n,
 \quad b_{rk}=\mathbb E[\bar D_r\bar D_k],                         \tag{4.5}
\]
and
\[
 \rho_k^e=\langle\bar C_k,\bar G_k\rangle_n
              -\mathbb E[\bar C_k\bar G_k].                       \tag{4.6}
\]
Unrolling (4.4) and comparing with (4.3) gives the exact, finite-\(n\) residual identities
\[
 \begin{aligned}
 R_k^S
 &:={\bar B}_{k}^{(n)}\bar H_k-\bar S_k
   =-2\delta\sum_{r<k}\bar e_r\bar D_r
          (\widehat a_{rk}^{(n)}-a_{rk}),\\
 R_k^P
 &:={({\bar B}_{k}^{(n)})}^{\!*}\bar D_k-\bar P_k
   =-2\delta\sum_{r<k}\bar e_r\bar H_r
          (\widehat b_{rk}^{(n)}-b_{rk}).                           \tag{4.7}
 \end{aligned}
\]
Thus (4.3) is exactly the Euler recursion only after passage to its population action law, where the three residual types in (4.5)--(4.7) vanish.

We now make that passage precise.  For \(k<N\), set
\[
 \zeta_{n,k}
 :=|\rho_k^e|
   +\sum_{r<k}\left(
       |\widehat a_{rk}^{(n)}-a_{rk}|
       +|\widehat b_{rk}^{(n)}-b_{rk}|
     \right).                                                       \tag{4.8}
\]
This is nonnegative.  Every term in (4.8) is a polynomially bounded empirical test of a fixed finite list of oracle program vectors.  The fixed-program theorem therefore gives
\[
 \max_{k<N}\zeta_{n,k}\longrightarrow0
 \quad\text{almost surely}.                                      \tag{4.9}
\]

All estimates below are made on a bounded event whose probability tends to one.  The bounds may be chosen independently of \(n\) and, for \(0<\delta\le1\), independently of \(\delta\) as long as \(k\delta\le T+1\).  Indeed, if \(M_k=\|C_k\|_\infty\), then boundedness of \(G\) gives
\[
 |e_k|\le1+a_0M_k,
 \qquad
 M_{k+1}\le M_k+2\delta a_0(1+a_0M_k),                             \tag{4.10}
\]
and discrete Gronwall bounds \(M_k\).  The same argument applies to \(\bar C_k\), with \(\bar C_0=0\).  The rank-one update then bounds \(B_k\) and \({\bar B}_k^{(n)}\) in operator norm, and their \(X\)-updates bound \(X_k,\bar X_k\) in normalized \(L^2\).  For the oracle \(P\)-bound one may use (4.3) directly and Cauchy--Schwarz on the deterministic coefficients \(b_{rk}\).  The initialization estimates and (2.13) supply the required initial bounded event.  A stopped version of the following argument removes any circularity in these bounds.

Couple the Euler network and the oracle with the same \(A_0,B_0\), and define
\[
 E_k:=B_k-{\bar B}_k^{(n)},
 \qquad
 r_k:=\|X_k-\bar X_k\|_n
       +\|C_k-\bar C_k\|_n
       +\|E_k\|_{\mathrm{op}}.                                    \tag{4.11}
\]
Then \(r_0=\|C_0\|_n=O_{\mathbb P}(n^{-1})\).  The residual identities give
\[
 \|R_k^S\|_n+\|R_k^P\|_n\le C_T\delta\zeta_{n,k}.                 \tag{4.12}
\]
Writing \(H_k=h(X_k)\), and using \(\|H_k\|_n\le a_0\), we obtain
\[
 \begin{aligned}
 \|H_k-\bar H_k\|_n&\le \|X_k-\bar X_k\|_n,\\
 \|S_k-\bar S_k\|_n
 &\le a_0\|E_k\|_{\mathrm{op}}
      +\|{\bar B}_k^{(n)}\|_{\mathrm{op}}
          \|H_k-\bar H_k\|_n+\|R_k^S\|_n
 \le C_T r_k+C_T\delta\zeta_{n,k},\\
 \|G_k-\bar G_k\|_n&\le\|S_k-\bar S_k\|_n,\\
 \|D_k-\bar D_k\|_n
 &\le\|C_k-\bar C_k\|_n
       +M_{C,T}\operatorname{Lip}(q)\|S_k-\bar S_k\|_n
 \le C_T r_k+C_T\delta\zeta_{n,k}.                                \tag{4.13}
 \end{aligned}
\]
Moreover,
\[
 \begin{aligned}
 |e_k-\bar e_k|
 &\le a_0\|C_k-\bar C_k\|_n
      +\|\bar C_k\|_n\|G_k-\bar G_k\|_n+|\rho_k^e|\\
 &\le C_T r_k+C_T\zeta_{n,k},\\
 \|P_k-\bar P_k\|_n
 &\le\|E_k\|_{\mathrm{op}}\|D_k\|_n
      +\|{\bar B}_k^{(n)}\|_{\mathrm{op}}
          \|D_k-\bar D_k\|_n+\|R_k^P\|_n\\
 &\le C_T r_k+C_T\delta\zeta_{n,k}.                               \tag{4.14}
 \end{aligned}
\]
Subtracting the \(X,C\) updates now yields
\[
 \begin{aligned}
 \|X_{k+1}-\bar X_{k+1}\|_n
 &\le\|X_k-\bar X_k\|_n+C_T\delta r_k+C_T\delta\zeta_{n,k},\\
 \|C_{k+1}-\bar C_{k+1}\|_n
 &\le\|C_k-\bar C_k\|_n+C_T\delta r_k+C_T\delta\zeta_{n,k}.       \tag{4.15}
 \end{aligned}
\]
Finally, from the two rank-memory updates and
\(\|u\otimes_n v\|_{\mathrm{op}}=\|u\|_n\|v\|_n\),
\[
 \begin{aligned}
 \|E_{k+1}\|_{\mathrm{op}}
 &\le\|E_k\|_{\mathrm{op}}
  +2\delta\|e_kD_k\otimes_nH_k
                -\bar e_k\bar D_k\otimes_n\bar H_k\|_{\mathrm{op}}\\
 &\le\|E_k\|_{\mathrm{op}}+C_T\delta r_k+C_T\delta\zeta_{n,k}.  \tag{4.16}
 \end{aligned}
\]
Adding (4.15)--(4.16) proves the closed recursion
\[
 r_{k+1}\le(1+C_T\delta)r_k+C_T\delta\zeta_{n,k}.                 \tag{4.17}
\]
Consequently
\[
 \max_{k\le N}r_k
 \le e^{C_T(T+1)}\left(r_0+C_T\delta\sum_{k<N}\zeta_{n,k}\right)
 \le e^{C_T(T+1)}\left(r_0+C_T(T+1)\max_{k<N}\zeta_{n,k}\right), \tag{4.18}
\]
which tends to zero in probability for every fixed \(\delta\), since \(N<\infty\).

The same proof applies to any prescribed finite family of additional action probes.  Unroll every occurrence of the learned \(B_k,B_k^*\), define the corresponding oracle action by replacing each normalized Gram coefficient by its population expectation, and add the finitely many absolute Gram deviations to (4.8).  Induction on the probe syntax, using (4.13)--(4.16), then gives convergence of every probe built with the bounded/Lipschitz state maps in normalized \(L^2\).  The fixed-program theorem controls the enlarged, still finite, \(\zeta\).  If an observable contains an unbounded factor multiplied by a bounded gate, such as \(q(J(X_k))P_k\), first truncate the unbounded factor at level \(M\).  The truncated map is Lipschitz; the oracle's fourth moments converge by the fixed-program theorem, and \(L^2\)-closeness transfers uniform square-tail control to the actual probe.  Letting \(M\to\infty\) proves convergence of the untruncated probe and of its squared empirical norm.  This proves the asserted fixed-mesh convergence of every finite action record, including outputs, kernels, and losses.  In its limiting action law, (4.7) vanishes and the bounded operator
\[
 B_k^\delta=B_0-2\delta\sum_{r<k}e_r^\delta D_r^\delta\otimes H_r^\delta
\]
satisfies \(S_k^\delta=B_k^\delta H_k^\delta\) and \(P_k^\delta=(B_k^\delta)^*D_k^\delta\); hence the population recursion is exactly the Euler scheme for (2.2).

## Replacement for the realization, uniqueness, and restartability part of Section 5

The one-time action records must first be enlarged by auxiliary cross-time records in order to place the limiting trajectory on fixed Hilbert spaces.  These auxiliary records will be discarded again after autonomy has been proved.

Let \(Q_T=\mathbb Q\cap[0,T]\).  Define the **rational path-probe grammar** to be the least countable two-sorted grammar with the following properties.

1. It contains right symbols \(X_q\) and left symbols \(C_q\) for every \(q\in Q_T\).
2. It is closed under rational linear combinations and under the particular coordinate constructions used in (2.2), including \(J,h,\arctan,q\), and it contains the designated product \(D_q=C_q q(S_q)\) once \(S_q=B_qh(X_q)\) has been formed.  (The product rule is needed only with the first factor \(C_q\), which has the uniform \(L^\infty\) bound proved below; no continuity assertion for multiplication on unrestricted \(L^2\times L^2\) is being made.)  In addition, for every finite tuple of same-side probes it contains the outputs of a fixed countable algebra of bounded globally Lipschitz cylinder functions which is dense in \(L^2\) for every Borel probability law on a Euclidean space; rational piecewise-linear tent functions suffice.
3. If \(v\) is a right probe and \(u\) is a left probe, then for every \(q\in Q_T\) it contains the left probes \(B_qv,B_0v\) and the right probes \(B_q^*u,B_0^*u\).

The recursion is countable because \(Q_T\), the cylinder algebra, and every finite stage of the grammar are countable.  It suffices below to take rational meshes \(\delta\downarrow0\).  For each fixed mesh \(\delta\), polygonally interpolate the population Euler variables and its rank-memory operator, and evaluate every finite path probe.  Each such evaluation is still a fixed finite tensor program: construct the finitely many required Euler times, unroll each learned operator into \(B_0\) and its finite rank memory, and append the finitely many \(B_0,B_0^*\) calls required by the probe.  Section 4 therefore supplies a deterministic population law for every finite same-side list of path probes and every same-side inner product.  Since the rational meshes, probes, and finite records are countable, all tensor-program convergence statements and the eventual \(B_0\)-operator bound may, when needed, be placed on one common probability-one event by countable intersection.  No program length is allowed to grow with \(n\).

For a fixed finite list \(P_1,\ldots,P_m\) of path probes, the same coordinate labels at finite width give a coupling of the mesh-\(\delta\) and mesh-\(\delta'\) empirical laws.  Equation (5.1), induction on the probe syntax, and the uniform operator bounds give
\[
 W_2\!\left(
   \operatorname{Law}_\delta(P_1,\ldots,P_m),
   \operatorname{Law}_{\delta'}(P_1,\ldots,P_m)
 \right)
 \le C_{T,P}(\delta+\delta').                                    \tag{5.2}
\]
For the newly added static actions one uses
\(\|B_0(v-\tilde v)\|_n\le M_0\|v-\tilde v\|_n\); for current actions one uses the analogous uniform bound for \(B_q\).  The product \(c q(s)\) obeys
\[
 \|c q(s)-\tilde c q(\tilde s)\|_2
 \le\|c-\tilde c\|_2+M_{C,T}\operatorname{Lip}(q)\|s-\tilde s\|_2, \tag{5.3}
\]
and all other generating maps are Lipschitz on the bounded state.  Taking \(n\to\infty\) in the finite-width coupling proves (5.2) for the deterministic population records.

Enumerate all finite joint-law and scalar-inner-product records and equip their product with the weighted sum of truncated \(W_2\) and absolute-value metrics.  The records are Cauchy as \(\delta\downarrow0\): first control finitely many entries by (5.2), then make the weighted tail small.  Every component space is complete.  Moreover, the subset of projectively consistent records satisfying the named linear, coordinate-map, operator-action, and adjoint relations is closed: marginalization and permutation are continuous in \(W_2\); the coordinate relations pass by their Lipschitz bounds, using (5.3) for the sole bounded-times-Lipschitz product; and the linear and adjoint relations pass through second moments.  The limiting records are therefore a consistent path-action law, not merely a collection of unrelated marginals.

We next realize these records.  Enumerate the right path probes and apply the Kolmogorov extension theorem to their consistent finite laws, obtaining a probability measure \(\mu_R\) on a countable product of copies of \(\mathbb R\); do the same on the left to obtain \(\mu_L\).  Let the named probes be the corresponding coordinate random variables.  Quotient their real linear spans by zero \(L^2\)-norm and complete.  Because the grammar contains a dense countable algebra of bounded Lipschitz cylinder functions, the resulting spaces are exactly
\[
 \mathcal H_R=L^2(\mu_R),\qquad \mathcal H_L=L^2(\mu_L).           \tag{5.4}
\]
All rational-time probes thus live on two fixed probability spaces, rather than on spaces depending on time.

The named matrix actions extend to bounded operators on these fixed spaces.  Indeed, on the product coupling used for the tensor-program theorem, (2.13) and Borel--Cantelli give \(\|B_0^{(n)}\|_{\mathrm{op}}\le M_0\) eventually almost surely.  Hence, for every formal right probe \(v\),
\[
 \|B_0v\|_{\mathcal H_L}\le M_0\|v\|_{\mathcal H_R}.             \tag{5.5}
\]
The same argument, using the uniform finite-time bound, gives
\[
 \|B_qv\|_{\mathcal H_L}\le M_{B,T}\|v\|_{\mathcal H_R},
 \qquad q\in Q_T.                                                  \tag{5.6}
\]
Thus zero-norm representatives are sent to zero-norm representatives, and the named actions extend uniquely by density.  Passing the finite identities
\(\langle u,B_qv\rangle_n=\langle B_q^*u,v\rangle_n\), and likewise for \(B_0\), proves that the two extensions are bounded adjoints.

The realization is continuous in time.  The uniform bounds on the polygonal Euler slopes pass to the limiting rational records and give, for \(q,r\in Q_T\),
\[
 \begin{aligned}
 \|X_q-X_r\|_{\mathcal H_R}+\|C_q-C_r\|_{\mathcal H_L}
   &\le M_T|q-r|,\\
 \|B_q-B_r\|_{\mathrm{op}}&\le M_T|q-r|.                         \tag{5.7}
 \end{aligned}
\]
For the operator assertion, first pass the finite-width inequality after applying \(B_q-B_r\) to an arbitrary formal probe, and then use density.  It follows that \(X,C\) extend uniquely and strongly continuously, and \(B\) extends uniquely in operator norm, from \(Q_T\) to all of \([0,T]\).

There is also a uniform essential bound on \(C\), which is stronger than its \(L^2\) continuity.  At every population Euler mesh, with \(M_k=\|C_k\|_\infty\), (4.10) gives
\[
 \sup_{k\delta\le T+1}M_k\le M_{C,T}.                             \tag{5.8}
\]
Therefore every rational-time limiting law of \(C_q\) is supported in \([-M_{C,T},M_{C,T}]\).  Countability gives this bound simultaneously for rational \(q\), and an \(L^2\) limit of uniformly \(L^\infty\)-bounded variables has the same essential bound.  Thus \(C(t)\in L^\infty(\mu_L)\) uniformly for all \(t\le T\).

Define on the fixed spaces
\[
 H(t)=h(X(t)),\quad S(t)=B(t)H(t),\quad G(t)=\arctan S(t),
 \quad D(t)=C(t)q(S(t)),\quad e(t)=\langle C(t),G(t)\rangle-1.    \tag{5.9}
\]
The maps \(H,S,G\) are strongly continuous.  Equation (5.3), the uniform \(L^\infty\) bound on \(C\), and continuity of \(S,C\) show that \(D\) is strongly continuous, and hence so is \(e\).  Consequently
\[
 t\longmapsto e(t)D(t)\otimes H(t)
\]
is continuous in operator norm, because
\[
 \|D_t\otimes H_t-D_s\otimes H_s\|_{\mathrm{op}}
 \le\|D_t-D_s\|_2\|H_t\|_2+\|D_s\|_2\|H_t-H_s\|_2.              \tag{5.10}
\]
It is therefore strongly measurable and Bochner integrable in
\(\mathcal B(\mathcal H_R,\mathcal H_L)\).  The vector-valued integrands \(eB^*D\) and \(eG\) are likewise continuous and Bochner integrable.

It remains to prove, rather than assume, the integral equations.  First let \(t\in Q_T\), and let \(\pi\) be a partition of \([0,t]\) with rational nodes.  The Riemann sums for the three continuous integrands in
\[
 \begin{aligned}
 X(t)&=X(0)-2\int_0^t e(s)B(s)^*D(s)\,ds,\\
 C(t)&=C(0)-2\int_0^t e(s)G(s)\,ds,\\
 B(t)&=B_0-2\int_0^t e(s)D(s)\otimes H(s)\,ds                     \tag{5.11}
 \end{aligned}
\]
are finite expressions in the rational path-probe records.  At mesh \(\delta\), the polygonal population Euler scheme satisfies the corresponding left-endpoint sums exactly.  The bounded, Lipschitz vector field changes their values by at most \(C_T(|\pi|+\delta)\) when they are replaced by the \(\pi\)-sums.  Hence the squared \(L^2\)-norm of each vector residual, which is one of the finite cross-time records, has limit at most \(C_T|\pi|^2\).  Letting \(\delta\downarrow0\) and then \(|\pi|\downarrow0\) proves the first two identities of (5.11).  For the third identity, apply the operator residual to an arbitrary formal right probe \(v\).  The same argument gives an \(L^2(\mu_L)\) residual bounded by \(C_T|\pi|\|v\|_2\).  Letting \(|\pi|\downarrow0\) proves the identity on a dense set of \(v\), and boundedness of both sides extends it to all of \(\mathcal H_R\).  Continuity extends all three identities from rational \(t\) to every \(t\in[0,T]\).  Thus (5.11), including its operator-valued Bochner integral, is a genuine equation on fixed spaces.

Uniqueness is now an ordinary dimension-free Gronwall argument.  If two solutions with the same complete initial action law are given on different realizations, first restrict each to the closed cyclic spaces generated by its initial saturated current-time grammar.  This restriction loses no part of either trajectory: its Euler iterates remain in the cyclic spaces, and the usual Euler-versus-solution estimate puts the continuous trajectory in their closure.  Now transport both restricted solutions to the canonical probability spaces generated by the common initial law.  Equality of all finite joint laws identifies the named cylinder algebras, and the saturation in item 2 makes the induced isometries onto the full \(L^2\) spaces; the recorded action and adjoint identities intertwine their initial operators.  On these common spaces, the derivation of (2.5)--(2.10) applies verbatim.  On any interval with the a-priori \(B\)-operator and \(C\)-essential bounds,
\[
 d(t)\le d(0)+L_T\int_0^t d(s)\,ds,
 \quad
 d(t)=\|X(t)-\widetilde X(t)\|_2
      +\|B(t)-\widetilde B(t)\|_{\mathrm{op}}
      +\|C(t)-\widetilde C(t)\|_2.                               \tag{5.12}
\]
Gronwall proves uniqueness when \(d(0)=0\).  In particular the path-action realization constructed above is independent of the auxiliary mesh sequence and of the chosen realization.

Finally, the cross-time records and the static \(B_0\)-tags are auxiliary existence data, not part of the Markov state.  At time \(t_0\), let \(\mathcal K_R(t_0),\mathcal K_L(t_0)\) be the canonical \(L^2\) spaces generated by the saturated **current-time** grammar starting from \(X(t_0),C(t_0)\) and the actions of the current \(B(t_0),B(t_0)^*\).  Euler iteration of (2.2) starting from that state never leaves these spaces: coordinate maps stay in the saturated coordinate spaces, current operator actions stay there by definition, and every update of \(B\) is a rank-one operator made from the current \(D,H\).  The Hilbert-space Euler estimate (the proof of (2.14) is unchanged) shows that the continuous restarted solution is the uniform limit of these iterates and also remains in the same two spaces.  Subtracting (5.11) at \(t_0\) gives, for \(s\ge0\),
\[
 \begin{aligned}
 X(t_0+s)&=X(t_0)-2\int_0^s e(t_0+r)B(t_0+r)^*D(t_0+r)\,dr,\\
 C(t_0+s)&=C(t_0)-2\int_0^s e(t_0+r)G(t_0+r)\,dr,\\
 B(t_0+s)&=B(t_0)-2\int_0^s e(t_0+r)D(t_0+r)\otimes H(t_0+r)\,dr. \tag{5.13}
 \end{aligned}
\]
Thus the shifted trajectory is a solution determined solely by the complete current action law.  Uniqueness identifies it with the solution freshly constructed from that law.  The resulting map on action-law equivalence classes is autonomous and satisfies
\[
 \Phi_{t+s}=\Phi_t\circ\Phi_s.                                   \tag{5.14}
\]
This also proves that discarding the auxiliary history tags loses no information that can affect the future.
