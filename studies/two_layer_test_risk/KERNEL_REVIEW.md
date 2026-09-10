# Internal adversarial review of the certificate arithmetic engine

Reviewer: `certified_error`, 2026-09-10. Verdict: **PASS for the stated
finite-rule arithmetic contract**, with no required correction remaining.
This is an internal implementation audit, not an isolated promotion review
or an audit of the final coefficient driver. I authored the Gaussian
cubature error lemmas, but did not author the kernel, its arithmetic proof,
or its retained check producer.

## Exact reviewed inputs and coverage

I read every line of certificate_kernel.cpp, CERTIFICATION_ENGINE.md and
check_certificate_kernel.py, and the full raw kernel_check result. I also
read the subsequent underflow clarification and complete executed-check
section in the final arithmetic proof. Frozen inputs are:

| Input | SHA-256 |
|---|---|
| certificate_kernel.cpp | `9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9` |
| CERTIFICATION_ENGINE.md | `52768b83be66674bf9895fd28ff1a2e3a84f138b646198b583f019b9066acb16` |
| check_certificate_kernel.py | `cc7f3fded02082eee118b5eecd0f947f39486eef27ea47d8095a828d62790be1` |
| compiled tested binary | `8c5b241801eaa4b8912989b9e404eb9693e63e94487661071c3bfa7044c189c7` |

The exact model/coefficient source and all locally required instructions
and skills were already read for the supporting error-certificate subtask.
AGENTS and workflow hashes were rechecked and were unchanged. This audit
uses the coefficient as a fixed input and does not reopen the population
flow or trajectory-remainder proofs.

## Mathematical and source reconstruction

1. **Elementary functions.** The degree-12 polynomial, reciprocal-factorial
   coefficients, 24 Horner operations, and eight squarings match the proof.
   I independently evaluated its three key scalar inequalities in exact
   Python Fraction arithmetic:

   ```python
   from fractions import Fraction as F
   from math import factorial
   u=F(1,2**53)
   gamma=lambda n:n*u/(1-n*u)
   delta=F(16,9)*gamma(25)+F(4,3)*F(1,4)**13/factorial(13)
   assert delta<46*u
   assert (1+46*u)**256*(1+u)**255-1<F(2,10**12)
   ul=F(1,2**64); n=401**3
   assert 4*n*ul/(1-n*ul)<F(15,10**12)
   ```

   All passed. Hence the relative exponential bound `2e-12` and absolute
   tanh bound `5e-12` follow from the proof rather than from the successful
   examples. In particular the numerator's cancellation near zero does
   not violate an absolute-error bound. The saturation branch has error
   below `3e-14`; large finite input cannot overflow `2*abs(z)` because
   that multiplication is skipped outside `|z|<=16`. The source uses no
   platform exp or tanh routine. The proof now explicitly includes possible
   underflow in the division by 256 as well as in Horner multiplication.
   This was a clarification supplied during audit; kernel bytes did not change.

2. **All primitive contractions.** Lower arrays are exactly `Q`, `L`, `T`
   in row-major `(a,b,i,j)` order. In the upper loop, training `S,H,d,dd`
   depend on the first three roots only. Conditional passive sums are
   `A=sum w H_x`, `B=sum w d_x`, `C=sum w dd_x`. Substitution into every
   returned array gives precisely the moments stated in the arithmetic
   proof. In particular dynamic `V` contains `S^2 B d_a`, and dynamic `C`
   contains `S A d_a d_b`; these are different contractions and the code
   preserves both. Both response derivative means are available to the
   driver; no full-four-dimensional term is replaced by an independent
   product or a smaller Gaussian marginal.

3. **Weights, mass and omitted roots.** Gaussian weights are not
   renormalized. Training arrays use three root masses, not four.
   Dynamic arrays retain the fourth mass when that root is numerically
   present. A fourth root is omitted exactly only when its entire factor
   column is zero: the source first verifies training fourth entries zero,
   then verifies the passive fourth entry zero for the omitted branch.
   Omitting the axis sets its sole weight to one. This is correct even for
   completely singular factors. Keeping an unnecessary zero factor axis
   instead gives its finite rule mass, whose error belongs to the Gaussian
   cubature bound. These two branches are distinguished in the tests below.

4. **Arithmetic enclosure.** I reconstructed the `1e-9` moment envelope
   under the six listed source/driver hypotheses. Node and dot-product
   errors fit inside the stated `1e-13`; adding them to the primitive
   bound gives activation error `6e-12`. The computed gate errors are
   bounded by `1.3e-11` for `d` and `2.6e-11` for `dd`: use derivative
   bounds two for `1-H^2` and four for `-2H+2H^3`, plus their evaluation
   rounding. The exact `|dd|=|tanh''(Y)|` is at most one, and its computed
   value is at most `1+2.6e-11`. Thus the arithmetic proof's looser printed
   bound `|dd|<=2` is not used repeatedly inside a product estimate; the
   sharper bound is available from the explicit polynomial, and products
   of computed factors only add the negligible multiplier
   `(1+3e-11)^5`. The weighted three-term `S` has error below `7e-12` when
   exact `sum|p|<=1`. Thus the actual highest-degree upper terms
   `S^2 d_x d_a` have product error below `4.1e-11`; terms containing
   `dd` have only one other activation or `S`, so their error is also
   below that scale. Lower `ddHH` products have error below `3.9e-11`.
   Weight error below `1.3e-11` and the proof's generous `2e-10`
   pointwise envelope therefore suffice. Positive exact masses are
   bounded by `1.000001^4`. The maximal outer count is `401^3`, not
   `401^4`, because passive inner sums are evaluated first; the
   long-double summation bound checked above covers both accumulations.
   The final cast and remaining products fit well inside the slack.
   The resulting error is strictly below `1e-9`.

5. **Parsing, dimensions and machine contract.** Input real values and
   output sums are transported as their exact binary64 bit patterns.
   The driver must compare parsed bits, not trust decimal text alone.
   IEEE binary64, nearest rounding, excluded fast-math/fused contraction,
   and long-double significand at least 64 bits are the operative machine
   hypotheses; they held for the tested GCC 11.4.0 x86_64 binary. Maximum
   counts `401^2`, `401^3`, `401^4` fit the reported 64-bit node counts.
   Bounds such as exact density-constant error, exact label norm, exact
   supplied radius, covariance difference and positive denominator remain
   explicit driver obligations. The kernel's floating precondition checks
   do not replace those rational checks. No accuracy claim for a floating
   root or solve is imported.

## Verification evidence

The author's retained check producer was fully inspected. Its degree-40
alternating exponential oracle, directed 180-bit squaring, and monotone
conversion to tanh provide rational primitive enclosures independent of
the kernel algorithm. The NumPy full-tensor comparisons are appropriate
indexing checks, not a claimed rigorous libm error theorem. The completed
run in `data/generated/two_layer_test_risk/kernel_check_20260910_01/`
passed all 19 primitive inputs and all listed contractions; maximum
contraction discrepancy was `5.88418203051333e-15`.

I separately tested the deliberately degenerate all-zero upper factor.
Then `H=S=dd=0` and `d=1`: every returned moment is exactly zero except
training `ddgram` and dynamic `dd`. These nonzero values must equal,
respectively, the product of three Gaussian finite-rule masses and the
product of three or four masses depending on the passive-axis branch.
Their reference intervals were computed with the retained exact rational
exponential oracle, not the kernel's own mass outputs. Both branches passed,
with maximum error `5.656108725018153e-15`.

I also checked that dropping a nonzero passive root fails with the message
`nonzero passive root omitted`. Primitive parsing, echoed bits and tanh
behavior passed at signed zero, the smallest normal positive binary64,
the smallest subnormal, and both largest-magnitude finite binary64 values.
All tests were finite arithmetic checks; no coefficient integral, training,
sampling or resolution campaign was executed by this reviewer.

The first scratch attempt had a reviewer test-harness error: an array
selector ending in `_bits` also selected the integer
`long_double_mantissa_bits`. It stopped with TypeError before making a
scientific comparison. That failed attempt is retained and labelled in
`kernel_review_20260910_01/result.json`. Restricting the selector to lists
fixed the test harness; kernel and mathematical inputs were unchanged.
The successful fresh run is `kernel_review_20260910_02/`, containing both
zero-factor outputs, primitive-boundary output and full result. Result hash:
`3432941e95840e15a020f01c0ae8943a4a08e59ecf7646a27fa9043b302c8ee5`.

## Complete reproduction source for the independent boundary checks

The reviewer owns this report only, so the exact reusable test source is
retained here rather than existing only in generated scratch. Run from
`/home/amir/Codes/PDE`, pointing `binary` at the binary produced by the
retained author's check recipe. Choose a fresh output directory.

```python
from pathlib import Path
from fractions import Fraction as F
import importlib.util, json, subprocess, hashlib
root=Path('/home/amir/Codes/PDE')
out=root/'data/generated/two_layer_test_risk/kernel_review_reproduction'
out.mkdir()
spec=importlib.util.spec_from_file_location(
    'oracle',root/'studies/two_layer_test_risk/check_certificate_kernel.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
binary=root/'data/generated/two_layer_test_risk/kernel_check_20260910_01/certificate_kernel'
normal=.3989422804014327; h=.5; p=[.25,-.125,-.0625]
elo,ehi=t.oracle_exp(F(1,8))
masslo=F(h)*F(normal)*(1+2*elo)
masshi=F(h)*F(normal)*(1+2*ehi)
results=[]
for omit in [False,True]:
    reals=[h,h,h,0. if omit else h,normal]+[0.]*16+p
    inp='upper\n1 1 1 '+('0' if omit else '1')+'\n'+' '.join(map(repr,reals))+'\n'
    v=t.invoke(binary,inp,reals)
    assert v['outer_points']==27
    assert v['total_points']==(27 if omit else 81)
    errors={}
    for name,values in v.items():
        if (not name.endswith('_bits') or not isinstance(values,list)
            or name in ['parsed_input_bits','grid_mass_bits']):
            continue
        power=(3 if name=='ddgram_bits' else
               (3 if omit else 4) if name=='dynamic_dd_bits' else 0)
        lo,hi=(masslo**power,masshi**power) if power else (F(0),F(0))
        error=max(max(abs(F(t.decode(b))-lo),abs(F(t.decode(b))-hi))
                  for b in values)
        assert error<F(1,10**9)
        errors[name]=float(error)
    results.append(dict(omitted_passive_axis=omit,
                        max_absolute_error=max(errors.values()),errors=errors))
    (out/('omitted.json' if omit else 'present.json')).write_text(
        json.dumps(v,indent=2)+'\n')
reals=[h,h,h,0.,normal]+[0.]*15+[.25]+p
bad=subprocess.run([str(binary)],
    input='upper\n1 1 1 0\n'+' '.join(map(repr,reals))+'\n',
    text=True,capture_output=True)
assert bad.returncode==1 and 'nonzero passive root omitted' in bad.stderr
values=[0.,-0.,2.**-1022,2.**-1074,
        1.7976931348623157e308,-1.7976931348623157e308]
small=subprocess.run([str(binary)],
    input='primitives\n6\n'+' '.join(map(repr,values))+'\n',
    text=True,capture_output=True)
assert small.returncode==0
v=json.loads(small.stdout)
assert v['parsed_input_bits']==[t.bits(x) for x in values]
for x,b in zip(values,v['tanh_bits']):
    actual=F(t.decode(b))
    target=F(x) if abs(x)<1 else F(1 if x>0 else -1)
    assert abs(actual-target)<F(5,10**12)
(out/'primitive_boundary.json').write_text(json.dumps(v,indent=2)+'\n')
result=dict(status='pass',zero_factor_cases=results,
    rejected_omitted_nonzero_axis=bad.stderr.strip(),
    subnormal_and_saturation_inputs=values,
    binary_sha256=hashlib.sha256(binary.read_bytes()).hexdigest(),
    oracle_source_sha256=hashlib.sha256(
        (root/'studies/two_layer_test_risk/check_certificate_kernel.py').read_bytes()
    ).hexdigest())
(out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Conclusion and scope left to the coordinator

This frozen kernel is suitable for the proposed certified moment evaluation
when its explicit driver hypotheses are checked. The primitive arithmetic
error may safely be added as `1e-9` per returned scalar. The final driver
must still charge Gaussian quadrature/tails, exact input-direction and
covariance errors, label rounding, interval algebra, clock normalization,
and angular integration. Passing this review alone proves no sign of `chi`.
No established file or Git index was modified by this reviewer.
