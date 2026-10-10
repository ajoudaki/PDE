"""Prepare scoped presentation corrections; preserve the frozen v1 packet."""
from pathlib import Path
import json

study = Path(__file__).resolve().parent
links = {
    'sec-mfp-finite-derivative-programs':('fixed finite derivative programs',''),
    'sec-mfp-physical-differentiation':('exact finite differentiation',''),
    'sec-mfp-source-evaluation':('Gaussian source-response evaluation',''),
    'sec-docs-special-data-limits-l3884':('adaptive Gaussian conditioning','12-three-sample-learning.qmd'),
    'sec-docs-special-data-limits-l4054':('causal scalar feedback','12-three-sample-learning.qmd'),
    'sec-docs-global-nonlinear-l1840':('contained probability and continuity specializations',''),
    'sec-docs-gaussian-calculus-l170':('derivatives along the gradient direction',''),
    'sec-docs-gaussian-calculus-l5338':('the finite MLP jet recurrence',''),
    'sec-docs-notation-l70':('the notation contract','notation.qmd'),
}


def corrected(text):
    for key,(label,path) in links.items():
        text = text.replace('@'+key, f'[{label}]({path}#{key})')
    return text


theory = study/'promotion_theory.qmd'
theory.write_text(corrected(theory.read_text()))
book = study/'promotion_book_patches.json'
patches = json.loads(book.read_text())
for patch in patches:
    patch['new'] = corrected(patch['new'])
book.write_text(json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
old = r'\counterwithout{corollary}{section}'
new = old+r'\counterwithout{definition}{section}'
(study/'promotion_quarto_patches.json').write_text(json.dumps([
    {'old':old,'new':new,'count':2}],indent=2)+'\n')
