# Internal weak-observable audit of theorem_v1

Audited input: the complete `studies/observable_hierarchy/theorem_v1.md`, as supplied to this scoped internal audit. No other route, study, source packet, or canonical dependency file was read. The earlier prompt-only weak candidate was already frozen before this audit. This is an internal mathematical audit, not an isolated promotion review or a verification of the external dependency packet.

Audited version-1 SHA-256: `6d6e85f31d15d0202c46602b91ecc76a3785166ecefd8d033ba44a7aa9e441ca`.

**Verdict:** the weak evolution, finite alphabet/level bounds, full-joint-law reconstruction, and reached restart arguments pass this internal audit, subject to the expressly cited canonical initialization/finite-width and uniform reference-tail results having the stated scope. I found no substantive mathematical gap in these parts. Two minor textual corrections are recorded below; neither changes the proof. In particular, the new Euler/one-reference comparison argument supplies the invariance and restart bridge missing from the prompt-only weak candidate.

## 1. Exact weak evolution and bounded sorts

The two-sort grammar is mathematically adequate. A B node has a deterministic finite envelope for each fixed program and fixed marks, because its leaves are constants, bounded activations, and the bounded readout; affine combinations and B-products preserve this property. It is not necessary that all B nodes share a bound independent of program, marks, or level. The readout estimate `80Y` is used only as a bound on the canonical interval, not as an assertion that the entire raw L² ball is bounded pointwise.

There is no illicit L² algebra step in the product differentiation. For bounded C¹(L²) paths B,C, write

\[
\frac{B(t+h)C(t+h)-B(t)C(t)}h
=B(t+h)\frac{C(t+h)-C(t)}h
 +\frac{B(t+h)-B(t)}h C(t).
\]

The first term tends to BC′ by the bounded-multiplier fact, and the second tends to B′C by bounded multiplication. The same fact handles continuity of the derivative. Action nodes satisfy the operator/Hilbert-space product rule because the action is C¹ in operator norm, which follows from the claimed C¹ Hilbert–Schmidt increment path. This justifies the Section 4 induction without ambient Fréchet smoothness or second temporal derivatives.

The reverse compiler has the correct adjoint orientations. For an `A b` node,

\[
\langle p,(Ab)'\rangle_2
=\langle A^*p,b'\rangle_1+\langle p,A'b\rangle_2;
\]

for an `A* b` node the two populations are exchanged. Substitution of
\(A'=-2\int r,d_2\otimes h_1\,d\mu\) therefore gives exactly the two products of expectations in (8). The moving row term includes \(u_1p_{w_1}+u_2p_{w_2}\), the upper readout term is \(E_2[p_c h_2]\), and all signs and factors of two agree with unhalved MSE and (2). Freezing `g,z₂⁰` is correct: these are retained initial observations, not another occurrence of the current action.

Every reverse covector is in L². Gate derivatives are bounded on the actual parent ranges; affine differentiation is scalar multiplication; reverse actions are bounded operators. The only unbounded scalar products in (7)–(8) have at most two L² factors, with possible bounded gates. In particular

\[
|E_1[p(1-h_1^2)q]|\leq\|p\|_2\|q\|_2.
\]

The proof does not silently retain a differentiable `d₁` response field. Its law is a well-defined bounded-gate pushforward of the joint law of `(q,z₁)`; its further temporal L² derivative is not invoked.

## 2. Reverse saturation and finite dependency

The compiler's use of `T_R(v)=R tanh(v/R)` is valid. Although it is not exactly the identity on a bounded interval, it obeys precisely the three properties needed here: pointwise convergence to the identity, \(|T_R(v)|\leq|v|\), and a 1-Lipschitz bound. For \(v_R\to v\) in L²,

\[
\|T_R(v_R)-v\|_2
\leq\|v_R-v\|_2+\|T_R(v)-v\|_2\to0.
\]

Each multiplication by a bounded local derivative is compiled as `b T_R(p)`, which is a permitted B-product. Each reverse action receives `T_R(p)`, a permitted B argument. Finite additions and affine scalar multiplications preserve sort L. Thus every compiled covector is an actual finite-alphabet program, not an unbounded query disguised as a coordinate.

Reverse induction remains valid at shared nodes: a finite sum of convergent incoming covectors converges in L², its saturation converges by the displayed inequality, and the next bounded operation preserves convergence. The same induction gives uniform-in-R L² bounds. Evaluation of the terminal scalar contractions need not introduce any new unbounded coordinate instruction; the existing joint law can be integrated against an at-most-quadratic, integrable function.

For each fixed characteristic observable, its covectors depend on its fixed marks and time, not on the new training integration variable. The error estimates in (8) are therefore uniform over that new input, because \(h_1,h_2,d_2,q\) have uniform L² bounds and the law has bounded labels. This validates passage of the R limit through the one training-law integral. The local time-uniform argument also works: exact covectors are continuous L² curves with compact images, and a 1-Lipschitz approximation converging at each fixed vector converges uniformly on a compact L² set by a finite-net argument.

The explicit node bound has ample room. Adding the scalar characteristic test costs at most n affine nodes and one trigonometric node. The stated edge bound covers binary affine/product instructions and unary gates/actions. Each reverse edge uses only a bounded number of saturation, local derivative, product, and accumulation nodes. Even retaining all intermediate covectors and duplicating their complete graphs separately for every contraction yields polynomial size far below the stated

\[
N=10^6(n+1)^6.
\]

There is no dependence on R or the number of training atoms: R enters real marks, while the new training input is one input mark outside the population-law dimension. The bound is intentionally loose but valid.

The exactness claim is correctly limited. The right side is a specified R limit inside one fixed higher level. The text does not claim a finite number of evaluations, a cutoff error rate, a closed finite system, or convergence of finite closures.

## 3. Finite population types, dimensions, and joint information

At fixed n, each instruction has finitely many discrete choices of operation, layer, and earlier parent positions. An ordered list of at most n output indices has finitely many possibilities. Hence a finite graph/type list follows independently of any coefficient values. The displayed graph-count upper bound is more than sufficient. At most three real coefficients per affine instruction and at most one circle direction per frozen forward seed give the stated program-mark bounds. A characteristic-function frequency adds at most n further real coordinates, explicitly identified separately in the text. This does not contradict the claim of finite-dimensional marks.

Population dimension is the number of selected output nodes, at most n. Taking unions of programs with different marks genuinely keeps their same-neuron joint values; it does not replace different marked probes by independent samples. Every finite collection of current and frozen fields appears at a finite level. This is the necessary information for contractions and for the well-definedness of the reconstruction map. Separate marginals would fail, but the candidate does not use them.

Bounded-gate pushforwards remain in P₂. The claimed fixed-tuple W₂ interpretation passes to such a pushforward once the underlying joint W₂ convergence is supplied: the map is continuous with linear growth, and W₂ convergence gives uniform integrability of the relevant squared L² coordinate. Quadratic contractions also converge under joint W₂ convergence by the corresponding product/uniform-integrability argument. These are consequences of joint W₂ information, not moment determinacy.

The finite alphabet also repairs the arbitrary-function-mark concern of the earlier broad weak route. Affine sine/cosine functions of finite word tuples are themselves finite programs and are L² dense in the tuple law. The Section 5 Fourier argument applies to the finite signed measure `f·law`, which is finite because `f∈L²` and the law is a probability measure. Gaussian convolution and the approximate-identity limit prove Fourier uniqueness without assuming that power moments determine a distribution.

## 4. Reconstruction of the relevant action

The finite-cylinder/monotone-class density step works even if the total marked family is uncountable. A sigma algebra generated by arbitrary coordinates is generated through finite cylinders and countable sigma operations; approximating indicators and then simple functions establishes the claimed L² density. No separability of the full ambient probability spaces is required.

Equality of every labeled finite joint law makes the identical-expression map representation independent. For bounded cylinders, equality of a zero squared norm transfers to the other realization. Products, signs, bounded Borel operations, and expectations transfer using the same joint law. The map extends to a surjective unital probability-algebra isometry; truncation handles the unbounded seeds.

The action-intertwining argument has the required dense domain. Bounded word values and their finite linear combinations are again bounded finite-word values, so actions on them are legitimate alphabet instructions. Density and boundedness extend intertwining to the whole observable-generated L² spaces. Applying the same argument to the actual adjoint gives the reducing-pair property, not merely a forward invariant subspace. This proves that an unobserved complementary action block cannot couple into the reconstructed subspaces through the current action.

No finite-level claim of complete operator recovery is made. Reconstruction uses all finite levels and only the generated subspaces, as permitted by the stated C-H1 contract.

## 5. Restart and uniqueness

I independently checked the estimate underlying (13), rather than assuming that repeated backpropagation necessarily preserves the cutoff dependence.

Let D be the raw sum distance on a fixed bounded pair of raw balls. Forward quantities and residuals have difference bounded by `C D`. Splitting

\[
d_2-\bar d_2=(c-\bar c)\phi'(z_2)
 +\bar c\,[\phi'(z_2)-\phi'(\bar z_2)]
\]

at the reference readout cutoff gives

\[
\|d_2-\bar d_2\|_2
\leq C(1+R)D+C\tau_R(\bar c).
\]

The action difference then gives the same form for \(q-\bar q\), since action norms are bounded and the difference of the middle actions is controlled by its Hilbert–Schmidt norm. The next split

\[
d_1-\bar d_1=(q-\bar q)\phi'(z_1)
 +\bar q\,[\phi'(z_1)-\phi'(\bar z_1)]
\]

adds `C R D+C τ_R(q̄)`; it does not multiply the earlier error by another R. Rank differences in the middle equation also add errors. Integrating and using bounded residuals establishes precisely the linear-in-R form of (13). No competitor tail or competitor L∞ bound is needed for this comparison. Raw L² boundedness controls the remaining factors.

The Euler invariance argument is then sound and avoids relying on tangency alone. The fixed observable-generated spaces are closed, stable under the required bounded coordinate operations, and reduce the current action. The ranks in an Euler update lie between them. The stated readout recursion gives a mesh-independent finite L∞ bound; row/action increments subsequently have mesh-independent bounds and speeds on any fixed remaining compact interval.

For the Euler interpolant, the distance from its current point to its last node is at most `V h`, where h is the largest mesh step. Comparing each node with the actual reference at the current time gives

\[
e'\leq C(1+R)(e+Vh)+CM e^{-aR}.
\]

Putting \(v=e+Vh\), taking \(R=1+a^{-1}\log(1/v)\) while \(0<v\leq1\), and increasing constants gives

\[
v'\leq L v[1+\log(1/v)].
\]

Its integrated bound is exactly the one intended in (14):

\[
v(t)\leq\exp(1-e^{-Lt})v(0)^{e^{-Lt}}.
\]

A first-exit argument validates the chosen range for sufficiently fine meshes. Euler convergence in the raw norm follows, proving that the actual continuation remains in the frozen observable spaces and its middle increments have only the supported Hilbert–Schmidt block.

Transport through the reconstructed isometries consequently gives an actual strong solution from the matching realization. Its increments preserve Hilbert–Schmidt norm; its original complementary action is left fixed. The action intertwining, multiplication, pairing, and Bochner-integral identities transfer each term of (2). Frozen seeds and all future word laws transfer as well.

Finally, the transported reference has the same c and q distributions at each input and therefore the same reference tails. Any competing strong continuation in the same affine raw space has bounded raw norms on compact intervals. Applying the one-reference estimate and the same logarithmic modulus with zero initial distance proves uniqueness after an ε regularization. This step does not assume tails on the competitor and does not silently infer restart from uniqueness of the original initialized path.

## 6. Dependencies and preserved objections

The following dependency claims were **not source-verified** in this scope. The internal proof uses them in explicit, identifiable places:

1. The canonical population path exists strongly on the stated common interval and law family, with the stated raw/action/readout bounds.
2. Its q fields have uniform integrated reference tails as in (12), including the needed reached-time restriction. The comparison form (13) itself is reconstructed above from elementary splits; the exponential tail source is external.
3. The complete alternating Gaussian source rule, including its reverse bulk, singular-query treatment, and common bounded action/actual-adjoint realization, covers the finite alphabet after bounded-product extension.
4. The fixed-program learned finite-width theorem covers arbitrary fixed finite repetitions of these bounded action instructions and the joint frozen/current observations, with the stated W₂ limit order.

The theorem gives enough concrete hypotheses to check where each is needed. This report does not certify their cited source statements or packet completeness. In particular, it does not replace the actual-adjoint Gaussian initialization by an isonormal embedding.

Two minor corrections should be retained in the revision record:

* **Section 6, lines 468 and 472:** the symbol `e` is first used for the error distance and then appears in `log(e/v)` as Euler's constant. Read literally with the already defined error, the logarithm has the wrong sign. The intended calculation is unambiguous from the next bound, but the display should read `1+log(1/v)` or use an explicitly distinguished constant. This is a notation correction, not a failure of the Osgood argument.
* **Section 3, line 184:** constructing `z₂⁰(v)` in the literal finite alphabet requires an affine `g·v` node, a tanh node, and an action node. Calling this “two instructions” suppresses the affine node. The accompanying `3n` extra-instruction bound already covers the correct count. Replace “two” with “three” or explicitly say the dot-product node is included separately.

The first correction was requested in the audit's message to the supervisor. The supervisor subsequently reported that version 2 replaces the ambiguous logarithm by `1+log(1/v)`, while preserving version 1. Version 2 was not read or audited here; this report and its hash remain attached to version 1. The second instruction-count wording correction is retained above as an additional minor request.

No additional substantive objection was found in the requested weak-evolution, finite-type, bounded-sort, cutoff, joint-law, dimension, or restart checks. The qualitative activation argument in Section 8 is also consistent with the physical factors in (2): the atom weights cancel the factor two in the initial readout velocity, and the two integrations produce the displayed half factors in the order-t² hidden increments. Its positive adjoint contractions use only well-defined L² pairings and bounded multipliers.

**Internal status recommendation:** retain as an internally checked C-H1 candidate after the two textual corrections and independent confirmation of the cited dependency packet. This audit establishes neither promotion nor C-H2 finite-closure results.
