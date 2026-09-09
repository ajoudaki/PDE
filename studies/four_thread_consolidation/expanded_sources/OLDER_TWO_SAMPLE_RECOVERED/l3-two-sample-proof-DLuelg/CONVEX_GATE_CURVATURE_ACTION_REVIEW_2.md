# Fresh isolated adversarial review 2

Candidate: `/tmp/l3-two-sample-proof-DLuelg/CONVEX_GATE_CURVATURE_ACTION.md`

Candidate SHA-256:

```text
e222051b6b85c07a23243b4c502ae6db4bbf7a2e7c659d0a4393e18f03522b2c
```

Reviewed version: 235 lines, 11,021 bytes. Review date: 2026-09-06.

## Verdict

**PASS for the stated conditional estimate and recursive-initial-law claims. No required mathematical correction found.** There are optional clarifications below, principally about the interpretation of the induced raw metric, the precise initialization assumption, and the norms in the historical-product limitation.

The central estimate (11) follows from the explicitly assumed path equations, energy identity, and second-moment symmetry. The scalar inequalities, bounded-monotone obstruction, modal factors, antiparallel endpoint, exact middle remainder, and Gaussian Gram argument survive the checks detailed below.

This is not a verdict on global population existence, preservation of symmetry, the validity of the assumed energy identity in a particular population construction, a finite-width limit, a historical-response estimate, or the unspecified full two-sample theorem. The candidate expressly does not prove those claims.

## Isolation and premise policy

I read the candidate in full, including every scope qualification. It was the only mathematical or contextual source read. No project files, histories, other reviews, skill instructions, external mathematical sources, experiments, or agents were used. The calculations and analytic examples below are deductions within this review, not empirical tests.

The existence and regularity of the path, its equations (6), the gradient/energy identity (7), the conditions on its initial readout and on `g`, and the imposed symmetry (8) are treated as premises. I checked their internal normalization and their uses; I did not require the candidate to establish them.

Section 4 is checked under its separately specified recursive centered Gaussian initialization. That initialization is not a consequence of merely assuming arbitrary bounded hidden operators.

Line references throughout refer to the candidate with the SHA above. Statements comparing this activation with an unnamed established proof or an unspecified desired theorem cannot be independently compared with those absent documents. No such comparison is used to justify the mathematical verdict.

## Findings requiring correction

**None within the candidate's stated scope.** In particular, the following are not defects in this conditional result:

- Not constructing the path whose existence is explicitly assumed.
- Not deriving the assumed symmetry from uniqueness.
- Not proving a positive lower bound for the contrast weight.
- Not estimating the unresolved middle and historical products.
- Not proving every-time motion, a finite-width limit, or the full two-sample theorem.

Conversely, the review does not silently upgrade any of those omissions into established results.

## Optional findings and minimal clarifications

### O1. Describe the first-field metric as the induced quotient metric

Location: lines 81–86 and 108.

The formula `E[v^T C^(-1)v]` is correct for the minimum raw norm needed to realize the pair of preactivation increments, and agrees with the full raw norm of the actual first-layer gradient, which lies in the span of the two inputs. An arbitrary raw parameter increment can additionally have a component orthogonal to both inputs. That component has positive raw norm and induces zero field increment.

The word “induced” supports the correct interpretation already. For complete precision, add “on the input span, equivalently the quotient by invisible raw directions.” This is a clarification of the geometry, not a missing factor or an obstruction to (7) or (11). The endpoint calculation below confirms the metric at `rho=-1` as well.

### O2. Specify the source population size in the finite-width tensor convention

Location: lines 111–112.

The matrix `uv^T/n` is correct when `n` is the size of the input population of that operator and both population inner products are empirical averages. It remains correct with unequal layer widths if the denominator is the source width. Writing `n_in` would remove a possible ambiguity. The matrix of this averaging operator should also be distinguished from a raw weight array if a separate convention rescales that array.

The normalized Hilbert–Schmidt calculation below verifies the convention actually stated in this candidate; it does not independently verify a separate, unstated finite-width parameterization.

### O3. Make the recursive law and the two label vectors explicit

Location: lines 206–226.

The section does condition its conclusions on the recursive Gaussian law. It would nevertheless be clearer to introduce it at the start as

```text
Sigma_1 = C,
Z^(ell) is centered Gaussian with covariance Sigma_ell,
K_ell[a,b] = E[phi(Z^(ell)_a) phi(Z^(ell)_b)],
Sigma_(ell+1) = K_ell,  ell = 1,2.
```

Also name the two label vectors as `(1,1)` and `(1,-1)`. Only the latter was explicitly designated a label vector earlier. Positive definiteness proves the stronger statement for every nonzero vector, so the present wording does not conceal a mathematical failure.

A useful extra sentence would be: “At the antiparallel first layer, individual feature maps are nonaffine, while the contrast is exactly affine.” The displayed identity at line 213 already entails this distinction; none of the existing claims contradicts it.

### O4. Specify the target norm when discussing historical products

Location: lines 194–197.

The claim of insufficient control is correct as a statement about unrestricted historical sensitivities. Its explanation could distinguish a population/time `L1` pairing from an `L2` product norm. They require different additional information. For the weighted plus mode, a Cauchy–Schwarz pairing requires a reciprocal-contrast-weight condition on the source, not merely an arbitrary unweighted second moment. Details appear in section 7 below.

This is an optional sharpening of a limitation, not an error in the bound or an assertion that the desired historical estimate is impossible.

## 1. Scalar softplus inequalities and global quantifiers

Locations: lines 9–38, equations (1)–(4).

For every finite real `z`, set `s=sigma(z)`. Then `0<s<1`, and direct differentiation gives

```text
phi'(z)  = s/10,
phi''(z) = s(1-s)/10 = p(z)-10p(z)^2.
```

Thus `0<p<1/10`, `0<phi''<=1/40`, and `phi>1`. The candidate's weaker non-strict lower bound `phi>=1` is valid. The second-derivative upper bound is attained at `z=0`.

For `p_x=p(x)` and `p_y=p(y)`, the exact factorization is

```text
phi''(x)-phi''(y)
  = (p_x-p_y) [1-10(p_x+p_y)].
```

Since `0<p_x+p_y<1/5`, the bracket has absolute value at most one. This verifies (3), including equal inputs and either ordering. There is no restriction to a bounded attained range.

Also `phi''=(1-sigma)phi'`, with `0<1-sigma<1`, so `phi''<=phi'`. If `x<y`, both derivatives are positive and

```text
|phi'(y)-phi'(x)|
  = integral_x^y phi''(z) dz
  <= integral_x^y phi'(z) dz
  = |phi(y)-phi(x)|.
```

Reversing the inputs handles the other ordering. Every constant in (2)–(4) is independent of the layer, configuration, path, `rho`, and time.

The later linear-growth claim also follows explicitly:

```text
log(1+exp(z)) <= log(2)+max(z,0),
|phi(z)| <= 1+log(2)/10+|z|/10.
```

This gives an `L2` composition bound on probability spaces. It gives no uniform feature ceiling. The candidate correctly identifies the loss of such a ceiling and does not reuse a pointwise readout bound from the unnamed old argument.

## 2. Obstruction for the bounded monotone class

Location: lines 40–68, equation (5).

The obstruction is valid under exactly the listed hypotheses. In particular, the proof does not need to assume in advance that `p'` is bounded, that `p` has only one maximum, or that `psi` is strictly increasing everywhere.

Here is the full chain with the relevant quantifiers made explicit.

1. Since `psi` is differentiable and nondecreasing, `p=psi'>=0`. Since it is bounded and monotone, its two endpoint limits are finite. The fundamental theorem of calculus, followed by monotone limits of the nonnegative integrals, gives

   ```text
   integral_R p = psi(+infinity)-psi(-infinity) < infinity.
   ```

2. Suppose (5) holds with a finite nonnegative constant `C`. Fix any finite `y`. Boundedness of `p` gives

   ```text
   |p'(x)| <= |p'(y)|+C|p(x)-p(y)|
            <= |p'(y)|+2C||p||_infinity.
   ```

   Hence `p` is globally Lipschitz and in particular uniformly continuous. No boundedness of `psi''` has been imported.

3. Nonnegative integrability and uniform continuity imply `p(x)->0` at both ends. If, for example, `p(x_j)>=epsilon` along a sequence tending to positive infinity, uniform continuity supplies a common interval radius on which `p>=epsilon/2`. A separated subsequence gives disjoint intervals with a fixed positive integral contribution, contradicting integrability. The negative end is identical.

4. Nonconstancy supplies a point where `p>0`, by the mean value theorem. Continuity and the two zero tail limits then force a positive global maximum `P=p(x0)` to be attained at a finite point. Since `p` is differentiable, `p'(x0)=0`.

5. Equation (5) now implies `|p'(x)|<=C|p(x)-P|`. On any finite interval to the right of `x0`, let

   ```text
   F(x)=integral_(x0)^x |p(u)-P| du.
   ```

   Then `F>=0`, `F(x0)=0`, and integration of the derivative inequality gives `F'<=CF`. Thus `exp(-C(x-x0))F(x)` is nonincreasing from zero and nonnegative, so `F=0` and `p=P`. Apply the same argument to `t -> p(x0-t)` for the left side. As the finite interval was arbitrary, `p=P` on all of `R`.

6. A positive constant on `R` is not integrable. This is the contradiction. The argument works for `C=0` as well. Negative constants cannot rescue (5); the usual domination-constant convention is nonnegative.

The even-gate observation also checks out. Here “gate” means the first derivative: if a differentiable gate `p` is even, then `p'` is odd. At a point with `p'(x)!=0`, the two equal gate values `p(x)=p(-x)` have unequal curvatures `p'(x)=-p'(-x)`. Consequently no finite difference-domination constant works at that pair.

The scope distinction at line 68 is essential and is respected: this is an obstruction to (5) for the specified class, not an obstruction to existence of a mean-field or gradient-flow solution, nor to every conceivable curvature estimate.

## 3. Raw metrics, signs, and the antiparallel endpoint

Locations: lines 72–89 and 103–122.

### First-field geometry for `|rho|<1`

Let `e_1,e_2` be unit input representers in raw parameter coordinates, with Gram matrix `C`. A raw increment `h` induces `v_a=<h,e_a>`. On their span, solving for the minimum-norm increment gives

```text
h_min = sum_a (C^(-1)v)_a e_a,
||h_min||^2 = v^T C^(-1)v.
```

Averaging over the first population produces the candidate's field metric. Raw components orthogonal to the two input representers are invisible in the field pair; they explain the quotient qualification in O1.

The first-field differential of `g` has ordinary covector

```text
b = (delta^(1)_1, -delta^(1)_2)/2.
```

The gradient for the `C^(-1)` metric is `Cb`, exactly the first-field equation in (6). There is no extra residual and no missing factor of two.

Writing `delta_+=(delta_1+delta_2)/2` and `delta_-=(delta_1-delta_2)/2`, its contribution to raw squared speed is

```text
E_1[b^T C b]
  = (1+rho)/2 ||delta^(1)_-||_2^2
    +(1-rho)/2 ||delta^(1)_+||_2^2.
```

This is nonnegative on the stated domain.

### First-field geometry at `rho=-1`

Now `e_2=-e_1`, and the realizable pair is `(Z,-Z)`. For a scalar increment `v`, the minimum raw squared norm is `v^2`, not `2v^2` or `v^2/2`.

The differential along `(v,-v)` is

```text
Dg[v] = E_1[(delta^(1)_1+delta^(1)_2)v]/2
      = E_1[delta^(1)_+ v].
```

Thus `Z'=delta^(1)_+` under the metric `E_1 v^2`. Substituting `rho=-1` directly in (6) gives the same pair velocity `(delta_+,-delta_+)`; it preserves the antiparallel constraint. The squared raw speed is `||delta_+||_2^2`, also the endpoint value of the preceding formula.

No inverse of the singular matrix is used at this endpoint. The separate treatment in the candidate is correct. `rho=1` is expressly excluded.

### Hidden and readout metrics

For probability-space Hilbert norms,

```text
(u tensor v)h = u E[vh],
||u tensor v||_HS^2 = ||u||_2^2 ||v||_2^2,
<u tensor v, a tensor b>_HS = <u,a> <v,b>.
```

At finite widths `n_in,n_out` with empirical-average norms, an ordinary operator matrix `A` has

```text
||A||_HS^2 = (n_in/n_out) sum_(i,j) A_ij^2.
```

The tensor therefore has ordinary matrix `uv^T/n_in`, and its norm is exactly the product of the two empirical second moments. This verifies the normalization used in (6) and (9).

For the readout metric, `D_(W4)g` is `(H^(3)_1-H^(3)_2)/2`, so the readout equation in (6) also has the correct normalization.

The energy identity is a premise in the population setting. Given that premise, zero initial readout indeed implies `g(0)=0`, and integration gives (7). In particular `g(S)>=0` also follows. The assertion about classical finite-dimensional feature-gradient paths is the ordinary chain rule for the smooth finite-dimensional function `g` with these fixed metrics; it does not assert a residual-based physical-time identity.

## 4. Scope of the `L2` field assertions

Locations: lines 74–101, 153–156, and 178–192.

At a fixed time, the stated assumptions are sufficient:

- The first preactivations are in `L2` by assumption.
- Linear growth of `phi` gives `H^(1)_a in L2`.
- Boundedness of `W^(2)` gives `Z^(2)_a in L2`; composition gives `H^(2)_a in L2`.
- The same reasoning through `W^(3)` gives `Z^(3)_a,H^(3)_a in L2`.
- The scalar readout is finite because `|f_a|<=||W^(4)||_2 ||H^(3)_a||_2`.
- Multiplication by the bounded gate preserves `L2`, so `delta^(3)_a in L2`.
- Bounded Hilbert adjoints preserve `L2`; alternating the two adjoints and the bounded gates proves the claims for `q^(2),delta^(2),q^(1),delta^(1)`.
- All feature and reverse half-sums and half-differences are in their respective `L2` spaces. In particular every displayed `kappa_ell` is finite at a fixed time.
- Bounded curvature gives `M^(3)_+`, `M^(3)_-`, and `phi''(Z^(2)_a)q^(2)_a` in `L2`.

The hidden velocities are sums of rank-one Hilbert–Schmidt operators, and the first-field/readout velocities have the required `L2` types. The initial hidden operators themselves need only be bounded; the proof does not silently require them to be Hilbert–Schmidt.

This argument establishes pointwise-in-time membership, not every desired time-integrated bound, differentiability statement, or product moment. Time regularity and the integrated chain rule are separately assumed. In particular it would be invalid to infer that every product of two displayed `L2` fields is again `L2`. The candidate does not do so: its later auxiliary product is explicitly treated separately.

## 5. Modal hidden gradient and the actual action estimate

Locations: lines 124–176, equations (8)–(11).

The modal gradient identity is for hidden layers `ell=2,3`. Expanding the two sample terms gives

```text
(delta_1 tensor H_1-delta_2 tensor H_2)/2
  = delta_- tensor U + delta_+ tensor V.
```

Thus the full hidden velocity has rank at most two; the individual modal summands are rank one. The signs and half-factors in (9) are correct.

The general squared norm before using symmetry is

```text
||delta_-||_2^2 ||U||_2^2
  +||delta_+||_2^2 ||V||_2^2
  +2<delta_-,delta_+><U,V>.
```

Also

```text
<U^(ell),V^(ell)>
  = (E_ell[(H^(ell)_1)^2]-E_ell[(H^(ell)_2)^2])/4.
```

Therefore (8) removes the cross term at both relevant input layers. This uses Hilbert tensor factorization and the imposed second-moment equality, not independence of the fields. The cross term printed at lines 149–150 is exactly the one otherwise present.

More precisely, the identity for `W^(2)` uses symmetry at layer 1, and the identity for `W^(3)` uses symmetry at layer 2. The top estimate (11) itself needs only the layer-2 equality. Assuming both equalities is permissible and also supports the middle-layer leading-term observation below. No layer-3 symmetry is needed for (11).

Since the populations are probability spaces and `U>=1` almost everywhere, `||U||_2^2>=1`. There is no missing population-mass factor.

For the top curvature comparison, put `p_a=phi'(Z^(3)_a)` and `c_a=phi''(Z^(3)_a)`. Then

```text
delta^(3)_- = W^(4)(p_1-p_2)/2,
M^(3)_-     = W^(4)(c_1-c_2)/2.
```

Equation (3) proves the difference bound after multiplication by `|W^(4)|/2`. For the plus mode, `0<c_a<=p_a` and `p_a>0`, so

```text
|M^(3)_+| = |W^(4)|(c_1+c_2)/2
          <= |W^(4)|(p_1+p_2)/2
          = |delta^(3)_+|.
```

Both comparisons are valid for negative, positive, and zero readout values. The use of the same readout factor is indispensable to this argument.

For each time at which the path equations hold, the full estimate is

```text
||M^(3)_-||_2^2 + kappa_2 ||M^(3)_+||_2^2
  <= ||delta^(3)_-||_2^2 + kappa_2 ||delta^(3)_+||_2^2
  <= ||delta^(3)_-||_2^2 ||U^(2)||_2^2
       +kappa_2 ||delta^(3)_+||_2^2
   = ||(W^(3))'||_HS^2
  <= ||theta'||_raw^2.
```

Integration and (7) give (11), with constant one. There is no change of neuron population, expectation of an unproved product, or omitted cross term in this derivation.

The scope of the uniformity claim at line 172 is correct: for every horizon and every `rho` in the stated range on which all premises hold, the numerical upper bound is one. It does not assert existence for arbitrarily long horizons or a uniform family of solutions. No division by `1-rho` occurs in the deduction.

The plus mode remains contrast-weighted. At times where `kappa_2=0`, its contribution on the left is zero and (11) supplies no unweighted control of that mode. Even when the weight is positive, extracting an unweighted estimate would require suitable lower-weight information. The candidate expressly avoids making that inference.

## 6. Exact middle remainder versus an auxiliary product

Location: lines 178–192, equation (12).

Use `p_a=phi'(Z^(2)_a)` in this section. Since `r_a=1-sigma(Z^(2)_a)=1-10p_a`,

```text
phi''(Z^(2)_a)q^(2)_a = r_a delta^(2)_a.
```

Taking the half-difference gives exactly

```text
N^(2)_- := [phi''(Z^(2)_1)q^(2)_1
            -phi''(Z^(2)_2)q^(2)_2]/2
          = r_+ delta^(2)_- + r_- delta^(2)_+.
```

There is no missing factor or interchange of modal signs. Furthermore,

```text
r_- = -5(p_1-p_2),
|r_-| <= 5|H^(2)_1-H^(2)_2| = 10|V^(2)|.
```

Since `0<r_a<1`, one also has `0<r_+<1` and `|r_-|<1/2`. The candidate's non-strict bound is valid.

Consequently the exact remainder

```text
R = r_- delta^(2)_+
```

is unconditionally in the layer-2 `L2` space at each time under the field premises:

```text
||R||_2 <= (1/2)||delta^(2)_+||_2.
```

The leading term does have an immediate action estimate:

```text
||r_+ delta^(2)_-||_2^2
  <= ||delta^(2)_-||_2^2
  <= ||(W^(2))'||_HS^2.
```

For the remainder, however, the corresponding modal action contains `kappa_1 ||delta^(2)_+||_2^2`. There is no assumed positive lower bound on `kappa_1`. The mere bound `|r_-|<=1/2` therefore does not supply a constant-one, horizon-independent action estimate for `R`.

Nor can the alternative pointwise upper bound `10|V^(2)delta^(2)_+|` be converted to such an estimate from two separate second moments. For example, on `(0,1)` with uniform measure, the functions

```text
A(t)=B(t)=t^(-1/4)
```

both belong to `L2`, while

```text
integral_0^1 |A(t)B(t)|^2 dt = integral_0^1 t^(-1) dt = infinity.
```

This analytic example establishes only the failure of a generic `L2 x L2 -> L2` inference. It is not a proposed trajectory counterexample. More structural information could alter the conclusion for a particular path.

Crucially, even if the auxiliary product is not in `L2`, the exact remainder remains in `L2` by its bounded coefficient. An infinite upper bound would simply be uninformative. Lines 188–192 maintain this distinction correctly and do not claim that every rewriting or every possible remainder estimate has been excluded.

Finally, the absence of a common scalar factor is a real obstruction to copying the proof of (10) directly: `q^(2)_1` and `q^(2)_2` are different adjoint fields in general. Neither positivity of the gate nor (3) permits treating them as the same readout.

## 7. Historical sensitivity limitation

Location: lines 194–197.

There is no hypothesis at all here controlling a historical source sensitivity. Thus (11), by itself, cannot imply a bound on an arbitrary product involving one.

The norm distinction in O4 can be made precise. On population-time measure, the minus-mode part of (11) gives `M_- in L2`. For a pairing with a source `J`, Cauchy–Schwarz would give

```text
integral |M_- J| <= ||M_-||_L2 ||J||_L2,
```

provided the extra source norm is finite and controlled. For the plus mode, the given quantity is `sqrt(kappa_2) M_+`; the corresponding pairing requires control of `J/sqrt(kappa_2)` wherever the weight is positive, and compatible treatment of the set where it is zero. An unweighted source second moment alone need not suffice.

If the goal instead is an `L2` norm of the product, separate second moments of the factors are insufficient; a joint product moment or stronger assumptions are needed. Boundedness of one factor or suitable fourth moments are examples of sufficient additional information, not assumptions of the candidate.

These observations support the candidate's limitation. They do not establish impossibility of a more structured, signed, or coupled estimate.

## 8. Recursive centered Gaussian initialization and nonaffinity

Location: lines 199–229.

### Individual nonaffinity

For a nondegenerate real Gaussian `G`, suppose `phi(G)=aG+b` almost surely. The difference `phi(z)-az-b` is continuous. Since the Gaussian density is positive on every real interval, a nonzero value anywhere would persist on an interval of positive probability. Therefore the difference must vanish on all of `R`. Twice differentiating would give `phi''=0`, contradicting (2).

This proves the asserted individual nonaffinity. It does not prove nonaffinity of every linear combination of two features, an issue made explicit by the antiparallel example below.

### First Gram for `|rho|<1`

Let

```text
K_1[a,b]=E[phi(Z_a)phi(Z_b)],  (Z_1,Z_2) ~ N(0,C).
```

The matrix is finite by linear growth and positive semidefinite by construction. If `c^T K_1 c=0`, then

```text
c_1 phi(Z_1)+c_2 phi(Z_2)=0 almost surely.
```

The Gaussian pair has a strictly positive density on `R^2`; continuity extends the equality to every pair of real arguments. Keeping the second coordinate fixed and varying the first forces `c_1=0`, because `phi` is strictly increasing. Varying the second then forces `c_2=0`. Hence the Gram is positive definite. This works for every nonsingular covariance, without requiring unit marginal variances at later layers.

### First Gram at `rho=-1`

The first pair is `(G,-G)`, with standard centered Gaussian `G`. Put

```text
A=phi(G), B=phi(-G), S_0=A+B, D_0=A-B.
```

Both moments are finite. Exchangeability under `G -> -G` gives equal Gram diagonals and

```text
lambda_+ = E[S_0^2]/2,
lambda_- = E[D_0^2]/2.
```

Here `S_0>=2`, so `lambda_+>=2>0`. The exact softplus identity gives

```text
D_0=G/10,
lambda_-=1/200>0,
kappa_1=E[(D_0/2)^2]=1/400.
```

The factor of one half in the eigenvalue formula is correct; it is distinct from the factor of one quarter defining `kappa_1`.

This also identifies an important potential overclaim that the candidate does **not** make: at antiparallel input, the first feature contrast is exactly linear in `G`. Strict convexity of the individual activation does not change that fact. The individual features are nevertheless nonaffine, and their uncentered Gram is positive definite. These statements are compatible.

### Propagation through the recursive law

Under the specified initialization, the next centered Gaussian covariance is the preceding **uncentered feature Gram**. The preceding calculations make that covariance finite and positive definite, including after the singular first input covariance at `rho=-1`.

The second pair therefore has full positive density on `R^2`. The same argument proves `K_2` positive definite. Its finite entries give a finite positive-definite covariance for the third Gaussian pair, and the argument proves `K_3` positive definite. Each marginal variance is positive, so the individual nonaffinity argument applies at all three layers.

Centered Gaussian preactivations do not imply centered features; the candidate correctly uses the uncentered second-moment matrix in the recursion. No joint coupling between different layers' Gaussian populations is needed for these separate initial-law conclusions.

Crucially, none of this derives the Gaussian recursion from an arbitrary choice of the bounded operators in section 2, or proves empirical convergence to it. The final initialization qualification explicitly limits the claim to the specified law.

### Readout and label modes

With the `L2` readout metric, the initial readout kernel is exactly

```text
K_3[a,b]=<H^(3)_a,H^(3)_b>.
```

Positive definiteness yields `c^T K_3 c>0` for every nonzero two-vector `c`, in particular the common and opposite label vectors. With the factor of one half in the definition of a label projection, the squared readout-gradient norm is `c^T K_3 c/4`. For opposite labels this is `kappa_3>0` initially.

Because the initial readout is zero, every reverse field is initially zero and both hidden matrix velocities are initially zero. Thus initial readout positivity would not prove initial all-layer motion. The candidate expressly disclaims the stronger motion conclusion.

There is also no uniform contrast gap as `rho` approaches one. For instance, the global `1/10` Lipschitz bound gives at the first initialization

```text
kappa_1
  = E[(phi(Z_1)-phi(Z_2))^2]/4
  <= E[(Z_1-Z_2)^2]/400
  = (1-rho)/200.
```

Strict positivity for each `rho<1` is consistent with degeneration in that limit. It does not undo the uniform numerical constant in the contrast-weighted estimate (11).

## 9. Scope and quantifier ledger

| Candidate location | Scope checked | Assessment |
| --- | --- | --- |
| Lines 3–7 | Activation discriminator and estimate on an existing path; no global construction, cutoff removal, limit, or every-time nonfreezing claim | Respected by the proof. |
| Lines 9–38 | One fixed activation, all layers/configurations, all real scalar arguments | Verified; no range restriction or tuned activation parameter is used. |
| Lines 40–68 | Every bounded, nondecreasing, nonconstant `C2` activation with bounded derivative fails (5) for every finite domination constant | Verified under the listed hypotheses; not an existence obstruction. |
| Lines 72–89 | Separate probability-space types, bounded hidden operators with HS increments, and `-1<=rho<1` | Internally consistent; induced-metric interpretation and antiparallel calculation are detailed above. |
| Lines 100–101 | Displayed forward/reverse fields are `L2` | Correct at each time under the field/operator premises; does not cover arbitrary products. |
| Lines 103–129 | Existing regular path, equations, energy, and layer-1/2 symmetry | Used as premises, not inferred from initialization or an unproved uniqueness statement. |
| Lines 118–122 | No claim of population differentiability merely from field definitions; no reference-cut or finite-width residual/clock assertion | No such step is used in the estimate. |
| Lines 137–151 | Modal orthogonality and action identity | Correct for hidden layers 2 and 3; cross term is explicitly retained when symmetry is absent. |
| Lines 158–176 | Top curvature domination and horizon/rho-independent numerical bound | Correct conditionally on the stated path premises; plus mode remains weighted. |
| Lines 178–192 | Exact middle remainder is `L2`; one auxiliary-product approach is insufficient | Correct; no assertion of impossibility for every alternative argument. |
| Lines 194–197 | No general historical-sensitivity or continuation estimate | Correct lack-of-control statement; norm-specific clarification is optional. |
| Lines 201–223 | Individual Gaussian nonaffinity and positive initial feature/readout Grams for every `rho` in `[-1,1)` | Verified under the specified recursive Gaussian law, including the singular first pair at `rho=-1`. |
| Lines 225–229 | Initialization only; no empirical-limit theorem or later-time/all-layer motion conclusion | Respected. |
| Lines 231–235 | Identified obstruction removed, feature ceiling sacrificed, larger response problem unresolved | Consistent with the proved statements. No claim about the truth of an absent full theorem is independently certified. |

The candidate therefore supports the advertised conditional curvature-action estimate, with the exact contrast weight and the stated limitations. None of the optional clarifications above is needed to repair its central inequalities or the Gaussian initialization proof.
