# Internal contributor check: initialized structure and angular scope

Reviewed artifact: `ONSET.md` in this study.

Originally reviewed frozen SHA-256:
`23d9c0885c39f8981f23c2a24102fe6392c5959327c82d6b6d03afca72195474`.

Final reviewed frozen SHA-256 after the scoped correction:
`ff2e3d72e8ba601482fb6fe61f1ef6dc38d38b78e464a513b4b2534f74ee462a`.

Both on-disk hashes were verified at their respective review stages. This report covers Sections
1 and 4–7, including their dependence on the immediate first-velocity identity
(3). Sections 2–3 beyond that identity belong to the separate flow check.
This is an internal contributor check by an author of some underlying
derivations, not an independent isolated review, promotion review, or approval
to alter established material. No experiments were run and no other study was
read. Only this report was written.

## Outcome

**PASS for the assigned structural scope at the final reviewed hash.** One
initialization-scope sentence required correction in the original artifact;
the correction is now verified. The order-one coefficient formula, Hermite representation, ranks
2/2/4, cubic readout selection, conditional parity comparison, and stated
Fourier limitations pass the checks below under the exact-expectation
hypotheses. No erroneous coefficient, sign, matrix orientation, or rank was
found in those claims.

The original Section 1 introduced arbitrary fixed closure order p and then stated:
“The source/response rule (H3.1) evaluates them”. H3.1 is the polynomial-core
contraction formula. It also covers bounded smooth retained tails depending
only on those core coordinates, but it does not cover every initialized word
at arbitrary p. A retained word introducing a new action requires the full
finite-source compiler. The book says this explicitly in
`docs/global_nonlinear.md:13276–13296`; the full rule is in Section 3.

The requested correction was to qualify H3.1 as applying to the core, in
particular p=1,2,3, and to cite the full finite-source rule for general p.
No change to Sections 4–6 was needed for this point because their orders have
no nonconstant appended words. The supervisor applied the correction, and
the new Section 1 explicitly limits H3.1 to p<=3 and directs retained new
actions at higher orders to the full Section 3 rule. That resolves the issue.
The supervisor also changed Section 3's onset wording to “first possible”
motion/effect, allowing vanishing coefficients. This second change introduces
no new structural claim; the separate flow checker owns the underlying
time-derivative formulas.

The difference was checked exactly by reversing these two textual changes
in memory and recovering the original SHA-256. Thus Sections 4–7 and all
other previously checked text are unchanged. No version of `ONSET.md` was
edited by this reviewer.

## Inputs and hypotheses

Scientific inputs were the complete `docs/observable_p1.md`, complete
`docs/NOTATION.md`, Section 3 of `docs/global_nonlinear.md`, its complete
relevant H3 initialization/dictionary/closure/parity/kernel passages at
13161–13790, and the frozen note above. The rigorous-math skill was read and
applied. Repository coordinates and physical time follow those sources.

The conclusions checked here require exact Gaussian coefficient and
population expectations; independent upper and lower population integration;
the joint lower law retaining the dependence of k on G; strictly positive
ridge; the prescribed state w(0)=G, c(0)=0, M(0)=D_p; bounded circle inputs
and labels; and the stated population-L2/Frobenius metric. Conditional
equality of p=1 and p=2 also requires common ridge and common coefficient
and population laws/rules with exact sign symmetry. Continuum trajectory
equality uses existence and uniqueness in the book's bounded-increment
characteristic class. No finite-node numerical symmetry is assumed for an
ordinary Halton prefix.

## Section 1: model, initialization, and normalization

The conditional-label reduction is valid: every state-dependent factor in
the gradient is a function of input and population marks, so integrating y
first replaces it with m(u)=E[y|u]. The noise contribution to square loss is
state independent. The signs and factor two in (2) match unhalved square loss.

The right inverse-Cholesky transpose in D is correct. If R_l=G_l+eta I,
then L_l L_l^T=R_l and

    L_l^{-T} L_l^{-1}=R_l^{-1}.

Thus the effective raw coefficient matrix in the initialized forward map is
R_2^{-1} C R_1^{-1}. For the separately designed raw matrix K, the displayed
conversion M=L_2^T K L_1 yields exactly

    b_2^T M E_1[b_1 h] = psi_2^T K E_1[psi_1 h].

That construction is correctly distinguished from prescribed D_p. The
original general-p use of H3.1 identified above is repaired in the final hash.

At c=0, d=q=0, so (2) immediately gives c'(0)=2S, M'(0)=w'(0)=0 and
f'(0)=2 K m. This verifies the first-velocity dependency used later without
extending this report to the higher time derivatives in Section 3.

## Section 4: the explicit order-one circle formula

For each coordinate, the lower nonconstant raw Gram block is
Sigma=[[v,beta],[beta,s_k]], and the corresponding upper nonconstant Gram
entry is tau. The raw contraction row is
(alpha v, alpha beta+tau gamma), including the reverse-response term.
All other-coordinate and constant pairings vanish by independence and
simultaneous sign reversal. These are the exact blocks of
`docs/observable_p1.md:77–156`.

At circle input u, the Gaussian pair (G_i,G dot u) has unit marginal
variances and correlation u_i. Consequently its lower feature-pairing vector
is (A(u_i),B_0(u_i)): integrating the independent reverse noise first turns
k_i into j(G_i). Applying the preceding raw matrix formula gives exactly

    Lambda(rho)=(tau+eta)^{-1}
      (alpha v,alpha beta+tau gamma)(Sigma+eta I)^{-1}
      (A(rho),B_0(rho))^T.

This establishes (9), followed by both formulas in (10). The shared letter
H_i for initialized upper coordinate features is distinct from the
input-indexed nonlinear hidden activation H_0(u); no identification between
them is used.

The Hermite series are also valid. With probabilists' Hermite polynomials
He_r, repeated Gaussian integration by parts gives
E[tanh(G)He_r(G)]=E[tanh^{(r)}(G)]=d_r, and similarly e_r for j. For each
fixed r, tanh derivatives are bounded, and differentiation of j is justified
by bounded chain-rule derivatives; Gaussian boundary terms vanish. Both
functions are odd, so their even coefficients vanish. The generating-function
identity for correlated standard Gaussians gives

    E[He_r(X)He_s(Y)] = 1_{r=s} r! rho^r.

Applying this first to finite Hermite expansions and then passing in L2
produces the displayed series. Parseval gives sum d_r^2/r!=v and
sum e_r^2/r!=E[j(G)^2]. Cauchy–Schwarz therefore bounds the sum of absolute
cross coefficients. Since |rho|<=1, the bounds establish absolute uniform
convergence, including the singular correlations rho=1 and rho=-1.
No temporal power-series convergence follows from this argument, and the
note correctly makes that distinction.

## Section 5: ranks, new odd channels, and parity comparison

For p<=3 the retained features are exactly the polynomial cores of dimensions
(5,3), (15,6), (35,10); see `docs/global_nonlinear.md:13223–13232`. H3.1 gives
the factorization in (11), with the feature-by-two derivatives oriented
correctly. Its rank is at most four. The positive-definite ridge factors are
invertible, so rank D equals rank C.

For p=1 the two coordinate rows are independent, because the h_i column in
row i equals alpha v>0 and vanishes in the other coordinate row. For p=2
the newly added total-degree-two features are even under full mark reversal.
Their pairings with h_i or H_i and their mean source derivatives vanish.
The raw contraction is therefore the order-one block with zero extra
rows/columns, proving rank two even if its ridge differs.

At p=3, write C=[U_1,U_2,B_1,B_2][A_1,A_2,V_1,V_2]^T. A zero combination
of the lower columns has, in the h_j row, v times the A_j coefficient.
Those coefficients vanish. In the k_j row the remaining relation has gamma
times the V_j coefficient, so all four coefficients vanish.

For the upper columns, P_3(H)=H^3-(EH^4/EH^2)H has mean zero and is
orthogonal to H. It is a linear combination of retained cubic and linear
raw features. Against this combination, B_j vanishes by orthogonality,
and all other-coordinate columns vanish by independence or because the
derivative is identically zero. The remaining U_j pairing is
E[P_3(H_j)Xi_j]/v by Gaussian integration by parts.

The note's strict positivity proof for that pairing is complete. Under the
probability measure weighted by H^2/EH^2, it is EH^2 times the covariance
of H^2 and atanh(H)/H. The latter ratio is strictly increasing in |H| by its
displayed integral representation. The weighted law has positive density
away from zero, so H^2 is not constant, and the independent-copy covariance
identity makes the covariance strictly positive. Integrability follows from
bounded powers of H and atanh(H)=Xi having Gaussian moments. Thus the two
U coefficients vanish. Testing the remaining relation against H_j gives
tau times each B_j coefficient, proving upper column rank four. A full
column-rank left factor is injective and the transposed right factor is
surjective, so their product has rank four.

The table's ranks and shapes are correct. The note correctly distinguishes
the full action rank from excitation by a given dataset, from the rank of
the nonlinear kernel, and from a Fourier cutoff. It also correctly declines
to infer a positive-semidefinite ordering of activated kernels from nested
raw spans.

For the flow comparison, full mark reversal preserves the laws and splits
the raw Grams, their positive-ridge Cholesky factors, and their inverses
into even and odd sectors. Initially D has only an odd-to-odd block. When
w and c are odd and M has this support, h is odd in lower marks, its even
feature pairings vanish, H is odd in upper marks, its gate is even, and d
has only odd coordinates. The vector field preserves the same subspace.
With a common ridge the surviving p=1 and p=2 factors and equations agree;
uniqueness yields identical flows. This matches the complete book argument
at `docs/global_nonlinear.md:13583–13681`.

The maintained ridges 1/4096 and 1/9216 do differ. Under exact population
expectations, a difference between these flows is not evidence that even
quadratic channels became active. The note is framed in exact expectations;
its normalization-only statement must not be exported to finite numerical
rules that also break sign symmetry.

## Section 6: actual cubic readout selection

For the balanced antipodal law, H_0(-e_1)=-H_0(e_1). Its label-weighted
average is therefore S=H_0(e_1), giving c'(0)=2H_0(e_1), as stated.
A(1)=v, B_0(1)=beta, and the zero-correlation values vanish by oddness and
independence. The initialized activation is tanh(a H_1), a=Lambda(1).

The positivity proof for a is valid. The conditional mean j(G) is odd and
strictly increasing, with the sign of h=tanh G; hence beta=E[h j(G)]>0.
Also

    (Sigma+eta I)^{-1}(v,beta)^T
      = (v(s_k+eta)-beta^2, beta eta)^T / det(Sigma+eta I).

Both entries are strictly positive: Cauchy–Schwarz gives beta^2<=v s_k,
v eta>0, and positive ridge makes the determinant positive. Both entries
of the contraction row are positive as well, so a>0.

Under the same H^2-weighted law, (12) is exactly EH^2 times the covariance
of H^2 and tanh(aH)/H. For positive x the latter ratio is strictly decreasing,
because tanh z-z sech^2 z has derivative 2z sech^2 z tanh z>0 and vanishes
at zero. The independent-copy covariance identity is therefore strictly
negative; the weighted law is nondegenerate and all integrands are bounded.
This proves the nonzero P_3 component of c'(0) for the displayed actual
training law. It concerns the unrestricted moving readout, not a retained
linear dictionary coordinate.

The general-label expression is the direct population inner product of
c'(0)=2 integral m H_0 dnu with P_3. The note appropriately permits it to
vanish. A polynomial in upper initialization marks is not thereby a circle
Fourier mode of the same degree; no such identification is made.

## Section 7: Fourier statement and scope

The formula using a Fourier matrix is correct when “on the uniform circle”
means that the training input marginal nu is normalized uniform circle
measure. Under that hypothesis the bounded kernel and bounded m are in L2,
and the Fourier matrix acts on m's Fourier coefficients as displayed.
The series for a fixed output coefficient is justified by Cauchy–Schwarz.
For a nonuniform training marginal, (3) remains correct but this particular
unweighted matrix formula requires the input measure to be included; merely
evaluating predictions on a uniform circle would not be enough. Stating
“when nu is uniform” would make the existing hypothesis more explicit.

At every represented state, oddness of tanh gives H(-u)=-H(u) and f(-u)=-f(u).
At initialization the kernel is odd in either argument separately. Under
uniform input integration it therefore has zero Fourier rows and columns
for even indices. This proves the even-mode exclusion without assuming any
mark or data symmetry beyond the uniform-measure hypothesis needed for the
Fourier operator formula.

Full input rotation stationarity is not asserted by the supplied book
(`docs/global_nonlinear.md:13721–13731`) and is not established by a
coordinate-axis polynomial dictionary. Thus replacing the Fourier matrix
by independent frequency eigenvalues is unjustified. The statement that a
cos(3 theta) target need not have a pure cos(3 theta) onset correctly avoids
asserting such a diagonalization; the note does not claim a computed
off-diagonal value or a particular frequency selection result.

The final limitations are appropriate: these are local initialized
contractions, not a trained endpoint, a monotone order-accuracy theorem, or
a numerical result. The book's arbitrary represented-state construction
showing no order-imposed odd-frequency cutoff does not become a training
selection theorem. This report does not certify any specific angular
coefficient as nonzero for a specified dataset.

## Scope of this outcome

This report supports the checked structural arguments at the final reviewed
hash, including the repaired general-p H3.1 sentence. It does not certify the Section 3 cubic flow
expansion, a numerical quadrature, a finite-width approximation, a broader
neural-flow horizon, or promotion to established documentation. Any modified
`ONSET.md` has a new hash and requires an explicit follow-up check of the
changed text; this final outcome refers to
`ff2e3d72e8ba601482fb6fe61f1ef6dc38d38b78e464a513b4b2534f74ee462a`.
