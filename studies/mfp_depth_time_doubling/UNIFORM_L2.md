# Depth two: exact causal response factorization and uniform-remainder audit

## 1. Verdict

For \(L=2\), each historical response coefficient is exactly divisible
by the step at which its Gaussian source first entered the trained state.
Sections 3--4 prove this and give closed causal tangent recursions. Thus
all past terms in the depth-two Gaussian DAG can be written as Volterra
sums carrying an explicit step weight.

This does **not** by itself prove

\[
 \left|F_{t,2}(2h)-F_{2t,2}(h)-\kappa_{\phi,2,t}h^3\right|
 \le C_{\phi,2}t^4|h|^5,\qquad |h|\le c_{\phi,2}/t. \tag{1.1}
\]

The remaining estimate is a horizon-uniform high-moment bound for the
causal tangent families and their mixed step/direction derivatives through
order four. The first inequality not controlled by the existing \(L^2\)
energy estimate is displayed in (6.2). A finite-horizon all-moment
induction proves finiteness, but its constant grows with the horizon.
No result in this study bounds it by total step variation alone.

Thus (1.1) is not proved here. This note narrows the depth-two open lemma
to an explicit coupled Volterra moment estimate; it does not relabel that
estimate as a theorem.

## 2. Exact depth-two population DAG

Use arbitrary real steps

\[
 \varepsilon_0,\ldots,\varepsilon_{N-1}. \tag{2.1}
\]

This includes all coarse, fine, and hybrid strings in the paired-Euler
argument. Write

\[
 u_s=Z_{1,s},\quad x_s=\phi(u_s),\quad
 z_s=Z_{2,s},\quad y_s=\phi(z_s), \tag{2.2}
\]

\[
 \delta_s=D_{2,s},\quad r_s=R_{1,s},\quad d_s=D_{1,s}. \tag{2.3}
\]

Let

\[
 Q_{rs}=\mathbb E[x_rx_s],\qquad
 K_{rs}=\mathbb E[\delta_r\delta_s]. \tag{2.4}
\]

The inverse-free width-first recursion is

\[
 a_s=A+\sum_{i<s}\varepsilon_i y_i,\qquad
 u_s=U+\sum_{i<s}\varepsilon_i d_i, \tag{2.5}
\]

\[
 z_s=\xi_s+
 \sum_{i<s}(\rho_{si}+\varepsilon_iQ_{is})\delta_i,
 \qquad y_s=\phi(z_s), \tag{2.6}
\]

\[
 \delta_s=a_s\phi'(z_s), \tag{2.7}
\]

\[
 r_s=\chi_s+\sum_{i\le s}\sigma_{si}x_i
       +\sum_{i<s}\varepsilon_iK_{is}x_i,
 \qquad d_s=r_s\phi'(u_s). \tag{2.8}
\]

The source blocks are independent and

\[
 \mathbb E[\xi_r\xi_s]=Q_{rs},\qquad
 \mathbb E[\chi_r\chi_s]=K_{rs}, \tag{2.9}
\]

while

\[
 \rho_{si}=\mathbb E[\partial_{\chi_i}x_s],\qquad
 \sigma_{si}=\mathbb E[\partial_{\xi_i}\delta_s]. \tag{2.10}
\]

These are formal cylindrical derivatives in one fixed chronological
expression of the source list. At a singular source Gram the individual
coordinate coefficients can depend on that expression; only their summed
adjoint action is intrinsic. The fixed operators \(I,J\) realize

\[
 \xi_s=Ix_s,\qquad \chi_s=J\delta_s, \tag{2.11}
\]

and the summed responses are the intrinsic adjoint identities for
\(J^*,I^*\). No covariance inverse occurs below.

## 3. Causal divisibility

### Lemma 3.1

For \(0\le i<s\le N\), there are cylindrical fields \(p_s^i,q_s^i\)
such that, identically as functions of the entire step vector,

\[
 \partial_{\chi_i}u_s=\varepsilon_i p_s^i,\qquad
 \partial_{\chi_i}x_s
 =\varepsilon_i\phi'(u_s)p_s^i, \tag{3.1}
\]

\[
 \partial_{\xi_i}\delta_s=\varepsilon_i q_s^i. \tag{3.2}
\]

Consequently

\[
 \rho_{si}=\varepsilon_i\bar\rho_{si},\qquad
 \bar\rho_{si}:=\mathbb E[\phi'(u_s)p_s^i], \tag{3.3}
\]

\[
 \sigma_{si}=\varepsilon_i\bar\sigma_{si},\qquad
 \bar\sigma_{si}:=\mathbb E[q_s^i] \tag{3.4}
\]

for \(i<s\). The current response is instead

\[
 \sigma_{ss}=\mathbb E[a_s\phi''(z_s)]. \tag{3.5}
\]

The quotients are defined by the displayed algebraic factorization, hence
also at \(\varepsilon_i=0\); no numerical division by zero is used.

#### Proof

We use mutual chronological induction. Its two assertions after the
forward pass at time \(s\) are

\[
 \partial_{\chi_i}u_s\text{ is divisible by }\varepsilon_i
 \quad(i<s),                                      \tag{3.6}
\]

and

\[
 \partial_{\xi_i}a_s,\ 
 \partial_{\xi_i}z_s,\ 
 \partial_{\xi_i}\delta_s
 \text{ are divisible by }\varepsilon_i
 \quad(i<s).                                      \tag{3.7}
\]

Both assertions are vacuous at \(s=0\). Suppose they hold through all
earlier nodes. The first assertion and the chain rule show that
\(\partial_{\chi_i}x_s\) is divisible by \(\varepsilon_i\), so (2.10)
shows that \(\rho_{si}\) has the same factor.

For \(i<s\), differentiate the readout sum in (2.5) with respect to
\(\xi_i\). Its \(j=i\) summand has the explicit factor
\(\varepsilon_i\); every \(j>i\) summand has that factor by the induction
hypothesis, and earlier summands are independent of \(\xi_i\). Hence
\(\partial_{\xi_i}a_s\) has the factor. In (2.6), the formal coordinate
\(\xi_s\) is held fixed when \(i<s\). In the \(j=i\) summand,
\(\rho_{si}+\varepsilon_iQ_{is}\) has the factor just proved; in a
\(j>i\) summand, \(\partial_{\xi_i}\delta_j\) has it by induction; a
\(j<i\) summand is independent of \(\xi_i\). The scalar Gram and response
nodes are deterministic coefficients for this formal source derivative.
Thus \(\partial_{\xi_i}z_s\), and then
\(\partial_{\xi_i}\delta_s\), have the factor.

It remains to advance the bottom assertion. Before \(\chi_s\) is exposed,
\(u_s,x_s\) are independent of that current coordinate. Differentiating
(2.8) with respect to an older \(\chi_i\) only differentiates the
\(x_j\)'s, which already carry \(\varepsilon_i\); differentiating with
respect to the current \(\chi_s\) gives one from the raw term. Therefore
the update

\[
 u_{s+1}=u_s+\varepsilon_s d_s                  \tag{3.8a}
\]

preserves the older factors and gives the new factor
\(\varepsilon_s\) for the current source. This closes the mutual
induction and proves (3.1)--(3.2). At the source time itself,

\[
 \partial_{\xi_i}\delta_i=a_i\phi''(z_i),         \tag{3.8b}
\]

because \(\xi_i\) enters \(z_i\) with coefficient one.

This is a syntactic identity in the chosen inverse-free chronology even
when its source Gram is singular. It does not assert uniqueness of an
individual partial coefficient under a different redundant coordinate
representation.

Taking expectations proves (3.3)--(3.4); (3.7) gives (3.5). Although the
individual barred coefficients inherit the chosen chronological
representation, the sums in (3.8)--(3.9) equal the fixed adjoint actions
and hence are intrinsic.
\(\square\)

### Corollary 3.2

Substitution into (2.6), (2.8) gives

\[
 z_s=\xi_s+\sum_{i<s}\varepsilon_i
       (Q_{is}+\bar\rho_{si})\delta_i, \tag{3.8}
\]

\[
 r_s=\chi_s+\sigma_{ss}x_s+
 \sum_{i<s}\varepsilon_i
       (K_{is}+\bar\sigma_{si})x_i. \tag{3.9}
\]

Thus no past response occurs without a step weight. This is stronger than
a row-sum estimate: it records the causal measure against which later
tangent equations must be bounded.

## 4. Closed response-tangent recursions

### 4.1 Bottom-source tangent

For fixed \(i\), set

\[
 p_s^i=0\quad(s\le i),\qquad p_{i+1}^i=\phi'(u_i). \tag{4.1}
\]

For \(s\ge i+1\), define

\[
 \widehat r_s^i=
 \sigma_{ss}\phi'(u_s)p_s^i
 +\sum_{j<s}\varepsilon_j
   (K_{js}+\bar\sigma_{sj})\phi'(u_j)p_j^i, \tag{4.2}
\]

\[
 \widehat d_s^i=\phi'(u_s)\widehat r_s^i
                 +r_s\phi''(u_s)p_s^i, \tag{4.3}
\]

\[
 p_{s+1}^i=p_s^i+\varepsilon_s\widehat d_s^i. \tag{4.4}
\]

Differentiate (3.9), \(d_s=r_s\phi'(u_s)\), and the bottom update
with respect to \(\chi_i\), then use (3.1). Response and Gram
coefficients are deterministic scalar nodes for this formal derivative.
This proves (4.1)--(4.4).

### 4.2 Top-source tangent

For fixed \(i\), put

\[
 q_i^i=a_i\phi''(z_i). \tag{4.5}
\]

For \(s>i\), define

\[
 \alpha_s^i=\phi'(z_i)+
 \sum_{i<j<s}\varepsilon_j\phi'(z_j)\zeta_j^i, \tag{4.6}
\]

\[
 \zeta_s^i=(Q_{is}+\bar\rho_{si})q_i^i
 +\sum_{i<j<s}\varepsilon_j
       (Q_{js}+\bar\rho_{sj})q_j^i, \tag{4.7}
\]

\[
 q_s^i=\alpha_s^i\phi'(z_s)
       +a_s\phi''(z_s)\zeta_s^i. \tag{4.8}
\]

After division by the factored \(\varepsilon_i\), these are respectively
the derivatives of \(a_s,z_s,\delta_s\) with respect to \(\xi_i\).
Together with (4.5), they prove (3.2) by induction.

Equations (2.4)--(2.5), (2.7), (3.3)--(3.5), (3.8)--(3.9), and
(4.1)--(4.8) are a closed inverse-free depth-two system. Every long
history sum is of Volterra form

\[
 \sum_{j<s}\varepsilon_j(\text{current--past kernel})
                         (\text{past field}). \tag{4.9}
\]

## 5. A horizon-uniform \(L^2\) energy bound

Let \(\mathcal K_s\) be the learned Hilbert--Schmidt connector part and

\[
 R_s=\|a_s\|_2+\|\mathcal K_s\|_{\rm HS}+\|u_s\|_2. \tag{5.1}
\]

The initialization connector has \(L^2\)-operator norm at most two.
With \(M=M_\phi\ge1\),

\[
 \|x_s\|_2\le M(1+\|u_s\|_2), \tag{5.2}
\]

\[
 \|z_s\|_2\le(2+\|\mathcal K_s\|_{\rm HS})\|x_s\|_2, \tag{5.3}
\]

\[
 \|y_s\|_2\le M(1+\|z_s\|_2),\qquad
 \|\delta_s\|_2\le M\|a_s\|_2, \tag{5.4}
\]

\[
 \|d_s\|_2\le
 M^2(2+\|\mathcal K_s\|_{\rm HS})\|a_s\|_2, \tag{5.5}
\]

\[
 \|\delta_s\otimes x_s\|_{\rm HS}
 =\|\delta_s\|_2\|x_s\|_2. \tag{5.6}
\]

Using \(M\ge1\) and
\((2+R_s)(1+R_s)\le2(1+R_s)^2\), these give

\[
 R_{s+1}\le R_s+6M^2|\varepsilon_s|(1+R_s)^2. \tag{5.7}
\]

Since \(R_0=2\), a first-exit argument proves

\[
 \sum_s|\varepsilon_s|\le\frac1{216M^2}
 \quad\Longrightarrow\quad \sup_sR_s\le3. \tag{5.8}
\]

Indeed, before a first exit from \(R\le3\), the total increase is at most

\[
 6M^2\left(\sum_s|\varepsilon_s|\right)4^2
 \le\frac49<1,
\]

which cannot carry the initial value two to three. Hence

\[
 \|x_s\|_2\le4M,\quad \|z_s\|_2\le20M,\quad
 \|y_s\|_2\le21M^2, \tag{5.9}
\]

\[
 \|\delta_s\|_2\le3M,\quad
 \|r_s\|_2\le15M,\quad \|d_s\|_2\le15M^2. \tag{5.10}
\]

Consequently

\[
 \mathbb E\xi_s^2\le16M^2,\qquad
 \mathbb E\chi_s^2\le9M^2. \tag{5.11}
\]

This estimate is completely horizon independent.

There is also a useful horizon-free exponential estimate for step-weighted
raw sources. If \(w_s\ge0\), \(\tau=\sum_sw_s>0\), and each centered
Gaussian \(G_s\) has variance at most \(V^2\), then convexity gives

\[
 \exp\!\left(\lambda\sum_sw_s|G_s|\right)
 \le\sum_s\frac{w_s}{\tau}
       \exp(\lambda\tau|G_s|).
\]

Therefore, without any independence assumption among the \(G_s\),

\[
 \mathbb E\exp\!\left(\lambda\sum_sw_s|G_s|\right)
 \le 2\exp\!\left(\frac{\lambda^2\tau^2V^2}{2}\right). \tag{5.12}
\]

By (5.11), (5.12) applies with \(V=4M\) to the \(\xi\)'s and
\(V=3M\) to the \(\chi\)'s. This confirms that a pathwise Volterra
argument need not pay for the maximum of \(N\) Gaussian coordinates.
It is an ingredient for the missing estimate, not yet that estimate.

## 6. The precise estimate still missing

The first top-source tangent contains

\[
 a_s\phi''(z_s)\zeta_s^i. \tag{6.1}
\]

An \(L^2\) estimate for (4.8) therefore needs

\[
 \|a_s\phi''(z_s)\zeta_s^i\|_2
 \le M\|a_s\zeta_s^i\|_2
 \le M\|a_s\|_4\|\zeta_s^i\|_4. \tag{6.2}
\]

Neither \(L^4\) quantity is controlled by (5.8). Estimating the \(L^4\)
tangent by the same recursion asks for \(L^8\); repeating an entrywise
Holder estimate through an arbitrary number of time steps asks for an
unbounded moment tower. The analogous bottom obstruction is

\[
 r_s\phi''(u_s)p_s^i \tag{6.3}
\]

in (4.3).

For each fixed finite horizon, the generated-core induction proves that
these fields have every finite moment. It does not prove a constant
independent of the number of recurrences. The fixed-\(t\) Price compiler
resolves the products by expanding the complete history and therefore
produces a \(t\)-dependent expression count.

A sufficient depth-two replacement can be stated without any output
quantity. Let a generated hybrid mean any coarse/fine history and
interpolation in the exact paired-Euler factorization. For \(0\le q\le3\)
one needs explicit \(H_{q,p}(\phi)<\infty,c_\phi>0\), for the finite list
of Holder exponents used by four-fold directional differentiation, such
that whenever

\[
 \sum_s|\varepsilon_s|\le c_\phi, \tag{6.4}
\]

all normalized mixed jets of (2.2)--(2.3), (4.1)--(4.8), and the
transported hybrid direction obey

\[
 \left\|t^{-q}\partial_h^q V\right\|_p
 \le H_{q,p}(\phi). \tag{6.5}
\]

The constants must depend only on \(M_\phi\) and stated Gaussian moments,
not on history length, Gram rank, or placement of coarse/fine steps.
The Volterra factors suggest a weighted Gaussian-moment or
Gaussian-Sobolev proof, but no such estimate is present here, and the
finite \(L^p\)-tower argument does not prove it.

The exact enlargement required for the paired-Euler defect is worth
recording. A hybrid interpolation introduces a generated parameter
direction \(\lambda\). Its response contains mixed fields

\[
 \partial_\lambda\partial_{\chi_i}x_s,\qquad
 \partial_\lambda\partial_{\xi_i}\delta_s, \tag{6.5a}
\]

and three \(h\)-derivatives of those fields. In the fixed-operator
realization, differentiating a later raw action also produces the new
coordinates

\[
 I(\partial_\lambda x_s),\qquad
 J(\partial_\lambda\delta_s), \tag{6.5b}
\]

which must be added to the chronological source list. They are not the
same operation as differentiating with respect to one old formal source
while holding all later raw coordinates fixed. Thus (4.1)--(4.8), which
control the undirected first source tangents, do not by themselves control
the mixed generated tangents (6.5a)--(6.5b).

At third \(h\)-order the two response families are also coupled at their
highest order: differentiating (4.2) produces terms
\(\partial_h^3\bar\sigma_{sj}\,p_j^i\), while differentiating (4.7)
produces \(\partial_h^3\bar\rho_{sj}\,q_j^i\). A valid closure must write
the enlarged mixed system, prove that its highest-order block is a
step-weighted causal operator with an explicit inverse bound, and bound
all lower-order forcing terms using (5.12). No such block-resolvent
estimate has been derived here. Merely saying “pathwise Gronwall” omits
this coupled-response step.

If (6.5) were proved, the paired-Euler lemma would give

\[
 \sup_{|h|t\le c_\phi}|A_{j,t}'''(h)|
 \le K_{\phi,2}t^3, \tag{6.6}
\]

with \(K_{\phi,2}\) an explicit polynomial in the \(H_{q,p}\). Summing
the \(t\) defects and using oddness would yield (1.1). Equation (6.6) is,
however, a consequence of the unproved (6.5), not a proof of it.

## 7. Why depth two does not inherit the Banach theorem

The obstruction appears with the first reused connector. In the fixed
realization

\[
 W_0=I+J^*,\qquad W_0^*=I^*+J, \tag{7.1}
\]

the maps \(I,J\) send an \(L^2\) vector to a Gaussian, but the adjoints are
only \(L^2\)-bounded. For \(p>2\), take
\(c\in L^2\setminus L^p\) and \(x=Jc\). Then \(x\) is Gaussian and lies in
every finite \(L^q\), whereas

\[
 J^*x=c\notin L^p. \tag{7.2}
\]

Hence no ambient estimate

\[
 \|J^*x\|_p\le C\|x\|_q \tag{7.3}
\]

can replace (6.5). Likewise, for non-affine \(\phi\), its Nemytskii map is
not \(C^2:L^2\to L^2\), since its formal second derivative contains the
unbounded product map \(L^2\times L^2\to L^2\). Thus the abstract
Banach-space paired-Euler hypotheses are not established at \(L=2\).

## 8. Consequence for larger depth

Lemma 3.1 suggests the depth induction. At every connector, a past
transpose response must cross the update at its source time before it can
affect a later forward query, and symmetrically for a past forward source.
Thus historical responses should admit step-divisible tangent kernels at
every fixed depth.

For \(L>2\), there is one coupled pair per connector, and each
forward/backward sweep couples adjacent pairs. An induction in \(L\) can
start only after a uniform moment norm closes (6.2)--(6.3) at one
connector. The causal factorization supplies the time weights; it does not
supply the missing norm estimate.

## 9. Self-audit

1. **Limit order.** All formulas are in the fixed-step width-first
   population DAG. No finite-width Taylor expansion or limit exchange is
   used.
2. **Reused-matrix dependence.** Both response families are retained. The
   current term \(\sigma_{ss}\), which is not step-divisible, is separate
   in (3.9).
3. **Zero steps.** Normalized kernels are defined by algebraic
   factorization, not numerical division.
4. **Singular Grams.** The proof uses a fixed syntactic source
   representation and never a Gram inverse. Individual partial
   coefficients are not claimed intrinsic; only their summed adjoint
   responses are.
5. **Uniform result.** Only (5.8) is claimed uniformly. The high-moment
   four-jet estimate (6.5) is explicitly unproved.
6. **No output-derived constants.** The missing quantities in (6.4)--(6.5)
   are stated on generated fields and response tangents, not through
   \(F_{t,2}\).
7. **Conclusion.** Causal divisibility is rigorous and useful, but
   insufficient to certify (1.1). Claiming the depth-two remainder from
   the present estimates would retain the gap in (6.2)--(6.5).
