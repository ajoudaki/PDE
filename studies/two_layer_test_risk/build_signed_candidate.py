"""Assemble canonical signed proof source in the study, never the live book.

The transformations change notation, placement and the formerly open sign
statement; the complete underlying reduction and error proofs are retained.
"""
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f'Expected one source fragment: {old[:100]!r}')
    return text.replace(old, new)


def canonical_section(text, title, prefix):
    text = re.sub(r'^# .+\n', title + '\n', text, count=1)
    text = re.sub(r'^## ', '##### ', text, flags=re.M)
    if prefix:
        text = re.sub(r'\b' + prefix + r'(\d+)\b', r'C4.' + prefix + r'\1', text)
    return text.strip() + '\n'


def main():
    base = (HERE/'PROMOTION_C4.md').read_text()
    base = replace_once(base,
        '### C.4. A controlled local risk expansion at equal training loss',
        '### C.4. Early test-risk improvement at equal training loss for a fixed tanh model')
    base = replace_once(base,
        'It proves a cubic expansion with a fourth-order remainder on the actual\n'
        "population flow. The coefficient's sign and nonvanishing remain open.",
        'It proves a strictly positive cubic test-risk difference, with a fourth-order\n'
        'remainder on the actual population flow. The sign proof includes a finite\n'
        'deterministic arithmetic certificate with all errors enclosed below.')
    first = base.index('The constants are independent of width and GD step;')
    last = base.index('The whole-circle predictions and risks', first)
    base = base[:first] + r'''The constants are independent of width and GD step; they are finite but
not numerically evaluated. The finite certificate below proves

\[
 \frac{27}{100000}<\chi<\frac{273}{1000000},\qquad
 \frac{35309}{1000000}<\beta<\frac{35311}{1000000}.
 \tag{C4.8a}
\]

Thus the cubic term is the first nonzero risk contribution. For
`t0=min(T,27/(200000M))`,

\[
 R(g_{\tau(t)})-R(f_t)\ge\frac{27}{200000}t^3>0
 \qquad(0<t\le t_0).
 \tag{C4.8}
\]

The initial risk is `1/2`; the leading benefit is about `0.000272 t^3`.
This establishes a small strict local improvement for this fixed design,
without a numerically evaluated time window or a practical magnitude claim.

''' + base[last:]
    base = replace_once(base,
        'Enlarge the finitely many constants to one `M>=1`. Inequality (C4.8)\n'
        'then follows from `Mt<=abs(chi)/2`.',
        'Enlarge the finitely many constants to one `M>=1`. Once the strict bound\n'
        '(C4.8a) is established below, `Mt<=27/200000` gives (C4.8).')
    base = replace_once(base,
        'If the separate sign premise in (C4.8) is proved, its positive minimum\n'
        'magnitude on every fixed `[delta,t0]` transfers that sign with probability\n',
        'The positive minimum in (C4.8) on every fixed `[delta,t0]` transfers\n'
        'the positive sign with probability\n')
    base = replace_once(base,
        'directions. These activity facts do not determine `chi`. If `chi=0`, a\n'
        'later coefficient is required; if a sign is eventually proved, it concerns\n'
        'only this fixed early-time comparison. No general feature-learning benefit,',
        'directions. These activity facts alone do not determine `chi`; its signed\n'
        'certificate below adds the test-risk conclusion for this fixed early-time\n'
        'comparison. No general feature-learning benefit,')

    err = (HERE/'CERTIFIED_ERROR.md').read_text().split('## Scope and provenance')[0]
    start = err.index('## 1. Analytic-strip')
    err = '# Gaussian cubature and covariance bounds\n\nAll expectations are normalized Gaussian expectations.\n\n' + err[start:]
    err = err.replace('The coordinator\'s independent whole-circle integration bound',
                      'The whole-circle integration bound below')
    err = err.replace('The displayed finite-sum inequalities\nwere independently evaluated in Python `Fraction` arithmetic on 2026-09-10;\nall three comparisons returned true. This was a scalar arithmetic check,\nnot a Gaussian-integral run. This file makes no post-result grid selection.\nThe executing producer\'s frozen configuration specifies which admissible\nchoice is used and records its hard arithmetic/runtime budget.',
                      'These finite-sum inequalities can be checked by integer arithmetic.\nThe executing certificate uses the dyadic grid specified below, which\nsatisfies these same strip, mass and tail inequalities.')
    err = canonical_section(err, '#### C.4 certificate: Gaussian integration and covariance', 'E')

    eng = (HERE/'CERTIFICATION_ENGINE.md').read_text().split('## Executed deterministic verification')[0]
    # Drop the author introduction, retaining every mathematical section.
    eng = '# Finite-sum arithmetic\n\n' + eng[eng.index('## Exact reduction'):]
    # The first provenance heading is deliberately identified, not guessed.
    for heading in ('## Executed component check', '## Executed verification', '## Executed checks'):
        if heading in eng:
            eng = eng.split(heading)[0]
    eng = eng.replace('[certificate_kernel.cpp](certificate_kernel.cpp)',
                      '[certificate_kernel.cpp](../code/tools/two_layer_risk/certificate_kernel.cpp)')
    eng = eng.replace("The root's driver", 'The certificate command')
    eng = canonical_section(eng, '#### C.4 certificate: the executing arithmetic', None)

    ang = (HERE/'ANGULAR_CERTIFICATE.md').read_text()
    ang = '# Circle integration\n\n' + ang[ang.index('## Statement'):]
    ang = ang.replace('`angle_error_bound.py`',
                      '[angle_error_bound.py](../code/tools/two_layer_risk/angle_error_bound.py)')
    ang = ang.replace('old numerical estimates', 'a floating estimate')
    ang = canonical_section(ang, '#### C.4 certificate: the circle rule', 'A')

    drv = (HERE/'DRIVER_CERTIFICATION.md').read_text().split('## Reproduction and ownership')[0]
    drv = '# Complete interval assembly\n\n' + drv[drv.index('## Input constants'):]
    drv = drv.replace('A preflight\naudit caught that inefficient ordering before any coefficient run; the\ncorrected order and an explicit trigonometric-width gate are independently\ntested and preserve the same rigorous interval semantics.',
                      'This order and the trigonometric-width gate keep the intervals\nusefully narrow while preserving rigorous enclosure.')
    drv = drv.replace('KERNEL_REVIEW and the deterministic\nkernel test provide independent verification, separately from that proof.',
                      'The supplied-state kernel checks independently test this implementation;\nthey are separate from the analytic error proof.')
    drv = drv.replace('preregistered', 'fixed').replace('predeclared', 'fixed')
    drv = drv.replace('conditionally authorized\ntarget B=30', 'optional\ntarget B=30')
    drv = drv.replace('ANGULAR_CERTIFICATE (A6)--(A7)', '(C4.A6)--(C4.A7)')
    drv = drv.replace('ANGULAR_CERTIFICATE', 'the circle-rule proof above')
    drv = drv.replace('CERTIFIED_ERROR (E1)--(E5)', '(C4.E1)--(C4.E5)')
    drv = drv.replace('CERTIFIED_ERROR (E6)--(E8)', '(C4.E6)--(C4.E8)')
    drv = drv.replace('CERTIFIED_ERROR', 'the Gaussian-error proof above')
    drv = drv.replace('CERTIFICATION_ENGINE', 'the arithmetic proof above')
    drv = re.sub(r'(?<!C4\.)\bE(\d+)\b', r'C4.E\1', drv)
    drv = canonical_section(drv, '#### C.4 certificate: exact interval assembly', 'D')

    conclusion = r'''
#### C.4 certificate: evaluated enclosure and reproducible decision

The complete fixed algorithm is
[certificate.py](../code/tools/two_layer_risk/certificate.py), its private
C++ kernel, and the exact angular-bound helper linked above. The
[tool guide](../code/tools/two_layer_risk/README.md) specifies the complete
input, arithmetic, resource and failure contracts, a fresh-output command,
an API example, and independent elementary-function and supplied-rule tests.
The mathematical coefficient and its inputs are fixed by (C4.1)--(C4.6).
Numerical linear algebra proposes dyadic root factors only; its accuracy
is charged by (C4.E6), not assumed. No retained array, study or Git history
is needed to regenerate the certificate.

At target `B=26`, the specified 256-angle rule, reduced to 64 evaluations,
and the certified root rules produce the enclosing interval

\[
 \frac{5358604107658561212253567}{19807040628566084398385987584}
 \le\chi\le
 \frac{21597479156841685713774185}{79228162514264337593543950336}.
 \tag{C4.32}
\]

It includes the full Gaussian-rule, covariance, elementary-function,
summation, input-constant, label, interval-rounding and circle-rule errors.
For the training clock the same execution gives

\[
 \frac{2797504526179671494928101665}{79228162514264337593543950336}
 \le\beta\le
 \frac{2797556156441557459457527739}{79228162514264337593543950336}.
 \tag{C4.33}
\]

Exact integer cross-multiplication places (C4.32)--(C4.33) strictly inside
(C4.8a), and in particular verifies the separate `|beta|<=1/10` premise
used for the circle bound. The displayed endpoints are approximately
`[0.00027054037037366814,0.00027259851133052906]` for chi and
`[0.03530947124611157,0.03531012291163362]` for beta; these decimal
displays do not decide any inequality. The angle bound obtained from
(C4.A9) is, more precisely,

\[
 D_8=\frac{41272525446939874982}{31640625},\qquad
 \frac{16D_8}{7\,256^8}
 =\frac{20636262723469937491}{127677049435953561600000000}
 <10^{-6}.
 \tag{C4.34}
\]

The evaluated calculation used 86,101,134 upper Gaussian nodes. The
complete mathematical bounds and executed finite arithmetic jointly
constitute a computer-assisted proof. Neither its positive output flag,
agreement at two resolutions, nor an unadjusted teacher projection would
alone prove the sign. A reproduced run may propose slightly different
dyadic factors on another supported platform; it certifies its own
enclosure only after all runtime contracts pass. The displayed enclosure
is the evaluated certificate, not a promised bit-identical result across
arbitrary platforms. The small local risk conclusion is exactly (C4.8),
with the finite-width and time limitations stated above.
'''
    result = '\n'.join((base.rstrip(), err, eng, ang, drv, conclusion.strip())) + '\n'
    # These names denote historical source files and may not survive in the book.
    for forbidden in ('CUBIC_DERIVATION', 'KERNEL_REVIEW', 'CERTIFIED_ERROR',
                      'CERTIFICATION_ENGINE', 'ANGULAR_CERTIFICATE',
                      'DRIVER_CERTIFICATION', 'studies/', '2026-09-10'):
        if forbidden in result:
            raise ValueError(f'Noncanonical source reference remains: {forbidden}')
    target = HERE/'PROMOTION_SIGN_C4.md'
    target.write_text(result)
    print(f'Wrote {target.name}: {len(result.splitlines())} lines')

    root = HERE.parents[1]
    guide = (root/'docs/README.md').read_text()
    guide = replace_once(guide,
        'but it does not answer the second question. This book presently develops tools\n'
        'and exact-capture results for the first, while keeping the second as the reason\n'
        'for studying the internal dynamics rather than only the training loss.',
        'but it does not by itself answer the second question. This book develops tools\n'
        'and exact-capture results for training. It also proves one small early-time\n'
        'test-risk improvement from hidden learning at equal training loss, for a fixed\n'
        'two-hidden-layer tanh model and a three-point design. This scoped,\n'
        'computer-assisted comparison is not a general explanation of generalization.')
    line = next(v for v in guide.splitlines() if v.startswith('| [Global nonlinear learning]'))
    guide = replace_once(guide, line,
        line[:-2] + ' C.4 proves a positive cubic test-risk improvement at equal training loss '
        'for one fixed two-hidden-layer tanh, three-point, uniform-circle design, '
        'using a complete finite arithmetic certificate; the positive local interval '
        'is width-independent but not numerically evaluated. |')
    guide = replace_once(guide,
        'arithmetic. Code execution is not needed\n'
        'to check the proofs; the displayed certificate has a complete reproduction\n'
        'command and independent checking routes.',
        'arithmetic. The earlier displayed polynomial certificate has a complete\n'
        'reproduction command and independent checking routes. The fixed tanh\n'
        'test-risk theorem in global-nonlinear C.4 is computer-assisted: its complete\n'
        'analytic error proof and executable finite arithmetic certificate are both\n'
        'parts of the proof. The opt-in tool regenerates all inputs and enclosures.')
    guide = replace_once(guide,
        'Gaussian joint depth/width/time theorem, or a generalization theorem. Their\n'
        'absence is not an impossibility result.',
        'Gaussian joint depth/width/time theorem, or a general iid-sample\n'
        'generalization theorem. The fixed-design comparison in C.4 does not supply\n'
        'those claims. Their absence is not an impossibility result.')
    guide = replace_once(guide,
        'and seeds. No currently included theorem relies on a numerical figure or a\n'
        'generated coefficient table.',
        'and seeds. The C.4 sign theorem depends on an explicitly bounded finite\n'
        'arithmetic calculation, with its complete producer and error proof retained.\n'
        'It does not infer a sign from a diagnostic table or a numerical figure.')
    (HERE/'PROMOTION_SIGN_DOCS_README.md').write_text(guide)


if __name__ == '__main__':
    main()
