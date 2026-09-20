# Informed internal audit of the unrestricted order-two/order-three theorem

2026-09-19. **Verdict: PASS for the complete frozen theorem. No mathematical correction is required.** At the exact canonical orders \(p=2,3\), every ambient local minimum attains the architectural loss floor for every finite dataset on the circle. For compatible labels that floor is zero. The candidate's statement that the same proof covers \(p=1\) also passes the dictionary check.

## Provenance and exact input

This is an explicitly informed internal review, not an isolated or promotion review. I authored dictionary_route.md and dictionary_counts.md and previously reviewed the finite-sample, rank-one, and constant-image proofs. I read the entire frozen candidate, including its reproduced necessary-condition and constant-image proofs. I did not read another study, abstract_route.md, or any order-two agent candidate.

| Input | SHA-256 |
|---|---|
| p2_p3_unrestricted_theorem.md | 1092fbbbebe969eee9286c4ede25a0fb694fe57f4801f9da456270d8c1d6a060 |
| finite_sample_theorem.md, previously reviewed | 5242bfda61ed94f2e5bda83b8843fe713d37dcbf4b7e2f204dc1ba8c23757c24 |
| constant_image_exclusion.md, previously reviewed | f513804bcbf7d0b2ff040be6f3cc6c179e7e1cb0d1428f44bf79934b7a71b305 |
| dictionary_route.md, reviewer-authored background | a95512882aa16474e6f6bd9ad0d4a88e3d9499d2b6976191188e4fa752079c53 |
| dictionary_counts.md, reviewer-authored background | 87ddaf612ff335f0829a9cc5103c74022786dfec04de4bc9749800319c1fa804 |
| docs/global_nonlinear.md | 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

The established scientific scope is complete C.4.7.9.2–4 and C.4.7.10.B, C.1, D.3, together with the notation contract. The exact dictionary check below concerns the later compatible dictionary of C.4.7.10, not the different pilot-list prototype in C.4.7.9. No external moment-range, purification, or Lyapunov theorem is a premise.

Only this review was written. The frozen candidate and all prior artifacts were left unchanged.

## 1. Exact full-dictionary and initialization check

The candidate uses the actual complete dictionary specified in C.4.7.10.B/C.1/D.3. At \(p=2\), the prefix indices are \(0,1,2\); at \(p=3\), they are \(0,1,2,3\). Codes 0 and 1 are the lower and upper constants already present in their respective polynomial lists. Codes 2 and 3 are the unbounded lower Gaussian seeds and are not retained bounded features. Thus neither order appends an extra raw feature. This conclusion deletes no prescribed word and does not silently substitute a polynomial core for a larger retained dictionary.

The actual retained counts are therefore

\[
 (d_1,d_2)=(15,6)\quad(p=2),\qquad
 (d_1,d_2)=(35,10)\quad(p=3).
\]

The core's lower law retains the reused-action response term \(p_j=\zeta_j+\alpha\tanh g_j\), with \(\zeta\) independent of \(g\), rather than replacing the reverse action by an independent unrelated field. Positivity of \(v,\tau,\alpha\) and the Gaussian density give the stated positive densities of \(X_1\) and \(X_2\) on their open cubes. Expectations remain on separate carriers.

The raw Gram matrices are positive definite: a polynomial relation holding almost surely holds on the open cube by density and continuity, and then is a polynomial identity; the Chebyshev products have distinct leading monomials. The exact inverse-Cholesky normalization preserves the full polynomial spans and preserves positive definiteness of the mark Grams. The ridge schedule is unchanged, with \(\eta_2=1/9216\) and \(\eta_3=1/16384\). The formula for \(D=L_2^{-1}CL_1^{-T}\) retains the correct right transpose and the book's actual contraction.

Consequently the effective lower coefficient space at these orders is all of \(\mathbb R^{k_1}\). This is crucial for the passage from the almost-sure lower-mark condition to \(r_iM^Td_i=0\), and it is actually verified here. Both mark columns are bounded on their physical carriers; their spans contain the constant; the upper span contains a nonconstant coordinate. The lower carrier is nonatomic because it retains \(g_1\) with its continuous law.

No numerical value of the prescribed initial matrix is needed for the ambient landscape theorem. Its invariance under the candidate's reasoning does not assert a new approximation theorem for arbitrary data laws or an unrestricted-horizon identification with the original neural dynamics.

## 2. Physical topology and the samplewise necessary condition

The displayed product metric uses the canonical population \(L^2\) pairings and the ordinary Frobenius coefficient metric. All lower-field and readout variations are admitted on the fixed joint mark carriers. The proof concerns the full ambient state space, not merely bounded-increment characteristics or states reached from initialization.

The finite-moment derivative calculation is valid at every admitted \(L^2\) state. Bounded marks and activation derivatives, together with \(E|c|<\infty\), give a locally uniform quadratic remainder in the finite moment array. The factors of two, residual convention, and the occurrence of the actual \(M^T\) are consistent with the unhalved weighted square loss.

For finite distinct-modulo-sign inputs, the input-ridge functions are independent even if the input vectors are linearly dependent. The hyperplanes excluded in selecting \(e\) are proper, and the odd Taylor recurrence gives the required nonzero coefficients and ordinary Vandermonde system.

The lower-subset replacement argument does not make the sample moments independent trainable variables. It changes one admissible field on a set of probability \(\varepsilon\), with squared \(L^2\) displacement \(O(\varepsilon)\), moment changes \(O(\varepsilon)\), and Taylor error \(O(\varepsilon^2)\). The strict first-order improvement has order \(\varepsilon\). The canonical atomless Gaussian coordinate supplies the needed small subsets of every positive-measure comparison set.

Matrix stationarity gives zero expectation of the nonpositive minimized odd function \(F_\omega(w)\). It therefore vanishes almost surely, and oddness makes the globally minimized function identically zero. Input-ridge independence separates its sample coefficients. The positive definite lower mark Gram then gives equation (6) in every coefficient direction. None of these steps depends on the number of samples relative to the dictionary dimensions.

## 3. Current-image condition

Because the lower Gram is positive definite, the function space

\[
 V_M=\{b_2^TMv:v\in\mathbb R^{k_1}\}
\]

is the full effective current image. In particular each current upper field \(z_i\) belongs to it. Every element is a polynomial in \(X_2\), and no assertion that this image contains the constant is made.

Equation (6) implies equation (8) for every direction in that image. For any \(k\in H^\perp\), the admissible change \(c+tk\) preserves predictions and residuals exactly. A sufficiently small equal-value displacement inside a local-minimum ball remains a local minimum on a smaller ball. Applying the same necessary condition before and after is therefore legitimate. The permitted nonzero \(t\) may depend on \(k\); the argument needs no uniform perturbation radius over directions.

Since \(h\phi'(z_i)\in L^2\) and \(H\) is finite-dimensional and closed, orthogonality to all of \(H^\perp\) gives the full inclusion (9) at each nonzero-residual sample. This is an inclusion for the available current image, not an unjustified enlargement to the whole dictionary. No Gram inverse, feature-rank bound, or free-moment perturbation enters this step.

## 4. Polynomial separation lemma

The new lemma is correct for any finite-dimensional real polynomial space \(V\) containing a nonconstant element and any finite list \(P_j\in V\), with no constant-in-\(V\) requirement.

If \(P_i\) is nonconstant, the choice \(h=P_i\) is an available image direction. Positive core density and continuity turn a putative almost-sure relation into an identity on the open cube. There is a real point of that cube where \(\nabla P_i\ne0\); otherwise all its derivative polynomials would vanish on an open set and hence identically. Choosing a real direction with nonzero directional derivative gives a real affine line with a segment in the cube and a nonconstant real polynomial restriction \(Q_i\).

Every nonconstant restricted polynomial has finitely many critical points in \(\mathbb C\). The equation

\[
 Q_i(t)=i\pi(n+\tfrac12)
\]

has at least one complex solution for every integer \(n\), by the fundamental theorem of algebra applied to the nonconstant polynomial minus that target value. Solutions belonging to different target values are distinct. Hence infinitely many such solutions exist, and one can avoid the finite union of critical points of every nonconstant \(Q_j\).

At that selected point \(t_0\), \(\cosh Q_i\) has a simple zero, because \(\sinh Q_i(t_0)\ne0\) and \(Q_i'(t_0)\ne0\). The numerator \(Q_i(t_0)=i\pi(n+\tfrac12)\) is nonzero. Thus \(Q_i\operatorname{sech}^2Q_i\) has a genuine double pole with nonzero leading coefficient.

Every \(\tanh Q_j\) has at most a simple pole at \(t_0\): the derivative of each nonconstant \(Q_j\) is nonzero there, and a constant \(Q_j\) is real and has no pole. A finite linear combination cannot have a double pole, even if poles coincide or coefficients cancel some simple parts.

The entire-function continuation supplied in the candidate is sufficient. Multiplying by \(\cosh^2Q_i\prod_j\cosh Q_j\) yields an identity between entire functions; it holds on a real segment and therefore everywhere. Away from the isolated denominator zeros it gives the original meromorphic identity. A small punctured neighborhood of \(t_0\) then contradicts the pole orders. Repeated, zero, opposite, constant, or otherwise dependent sample polynomials cause no exception.

If \(P_i\) is constant, its gate is a strictly positive real constant. Select any nonconstant \(h\in V\) and a real line on which it restricts to a nonconstant polynomial \(Q\). On that line, real-analytic continuation turns the putative relation into a real-line identity. The nonzero constant multiple of \(Q\) is unbounded, whereas the finite tanh sum is bounded. This contradiction covers the case where all sample fields are constant but the current image still contains a nonconstant unused direction.

The complex or real continuation outside the cube is used only to disprove a functional identity. It does not require physical mark values outside their bounded support, nor does it introduce nonphysical parameter perturbations.

## 5. Constant and zero current images

The reproduced remaining argument is complete and correct. If \(V_M\subseteq\operatorname{span}\{1\}\), each matrix column represents a constant, giving \(b_2^TM=v^T\). For \(v\ne0\), equation (6) at any nonzero-residual sample forces \(Ec=0\); for \(v=0\), every upper field is zero without that condition. In either case the predictions are zero for every lower-field change with the same \(M,c\).

If \(E[b_2c]\ne0\), matrix stationarity at all nearby equal-value lower fields gives equation (13) after cancelling a nonzero outer-product factor. A bounded truncation of the lower field can be selected arbitrarily close in \(L^2\), and hence remains a local minimum. For a fixed constant endpoint \(s\), the interpolation from that bounded field has a locally uniform pole-free complex neighborhood at every real parameter value. Integration against bounded marks preserves holomorphy; the outer gates also have pole-free local neighborhoods. Consequently the identity near parameter zero extends along the real line to the constant endpoint. No analyticity of an unbounded starting field is assumed.

At that endpoint the modified ridges are \(h_\kappa(t)=\tanh(t)\operatorname{sech}^2(\kappa\tanh(t))\). They are odd, bounded and real analytic, with derivative one at zero, so they have infinitely many nonzero odd Taylor coefficients. Choosing any \(m\) such coefficients gives a generalized Vandermonde system. Its invertibility follows from the stated induction and Rolle bound for positive roots of a polynomial with at most \(m\) monomials. Thus equation (14) forces zero residuals and proves the necessary condition \(E[b_2c]=0\).

For \(v=0\), an arbitrarily small constant readout change preserves predictions but contradicts that condition since \(E b_2\ne0\). For \(v\ne0\), an arbitrarily small centered nonconstant mark readout change preserves the zero mean and all predictions, but changes \(E[b_2c]\) by a nonzero vector detected by the positive variance of the chosen mark. Both changes remain in the stated \(L^2\) topology. This exhausts all constant and zero images.

## 6. Attainment, grouped observations, and scope

The rank-one attainment construction is valid for every finite list of distinct-modulo-sign directions. Its upper coordinate \(X_{2,1}\) has positive density on \((-1,1)\), so the same Taylor/Vandermonde argument makes the finite readout feature Gram positive definite. The constructed readout is a bounded finite linear combination and fits every label. No uniform conditioning claim is needed.

Bias-free input oddness holds at every state. The signed grouping identity (15) is the exact weighted variance decomposition, with positive grouped weights and finite grouped labels. Applying the theorem to the representatives makes every local minimum attain its explicit irreducible floor, with no bound on the number of groups.

The same dictionary and proof checks hold at \(p=1\): its full raw lists are the degree-one polynomial cores with dimensions \(5,3\), and no tail entries are added. Thus the candidate's closing extension to \(p=1\) is justified. No extension to other orders is established by this review: later full word tails and possible coordinate redundancies require their own analysis.

PASS certifies the internally reviewed finite-data landscape proof for the exact canonical orders stated. It does not imply convergence of initialized training, bounded iterates, an optimization rate, a finite-particle theorem, an infinite-data theorem, or promotion into established material.
