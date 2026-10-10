#!/usr/bin/env python3
"""Assemble the complete compact proof as a native Quarto chapter.

Inputs are frozen study-owned TeX files.  No book or source input is mutated.
Run from any directory; the sole maintained output is promotion_compression.qmd.
The source-label map and mechanical inventory go to study-owned generated scratch.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SCRATCH = ROOT / 'data/generated/book_promotion_20261010/draft_compression'
INPUTS = ['compact.tex', 'compact_fitting.tex', 'compact_foundations.tex',
          'compact_legendre.tex', 'compact_selected.tex']
FORMAL = {'theorem': 'thm', 'proposition': 'prp', 'lemma': 'lem', 'claim': 'lem',
          'definition': 'def', 'remark': 'rem', 'corollary': 'cor'}


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def balanced(s, start):
    assert s[start] == '{'
    level = 1
    i = start + 1
    while level:
        if s[i] == '{' and (i == 0 or s[i-1] != '\\'):
            level += 1
        elif s[i] == '}' and (i == 0 or s[i-1] != '\\'):
            level -= 1
        i += 1
    return s[start+1:i-1], i


def braced_macro(s, command, replacement):
    pat = re.compile(r'\\' + re.escape(command) + r'\s*\{')
    while m := pat.search(s):
        body, end = balanced(s, m.end()-1)
        s = s[:m.start()] + replacement(body) + s[end:]
    return s


raw = {f: (HERE/f).read_text() for f in INPUTS}
main = raw['compact.tex']
main = main[main.index(r'\section{Setup'):main.index(r'\end{document}')]
start = main.index(r'\paragraph{What must be remembered.}')
stop = main.index(r'\begin{theorem}', start)
main = main[:start] + main[stop:]
for f in INPUTS[1:]:
    main = main.replace(r'\input{' + f[:-4] + '}', raw[f])
main = main.replace('the older decoder, numerical setup-cost alternatives and empirical material\n'
                    'are outside this theorem-focused copy.',
                    'these statements concern exact arithmetic and do not assert efficient\n'
                    'preprocessing or empirical performance.')

# The three inline verifications are full proofs in the source. Give them
# explicit proof divisions without changing any argument.
main = main.replace(r'\emph{Verification of the local claim.}',
                    r'\begin{proof}[Order-independent physical bounds]')
main = main.replace('just defined remain private to this construction proof.',
                    'just defined remain private to this construction proof.\n\\end{proof}')
main = main.replace(r'\emph{Verification.}', r'\begin{proof}')
main = main.replace('which proves \\eqref{cp:eq-innovation}.',
                    'which proves \\eqref{cp:eq-innovation}.\n\\end{proof}')
main = main.replace('No recursive matrix central limit theorem is needed.',
                    'No recursive matrix central limit theorem is needed.\n\\end{proof}')

# Preserve the unrelated generating-function indeterminate under its original
# name: it is protected from readout replacement below.
main = main.replace('$(1-2xw+w^2)^{-\\nu}=\\sum_j C_j^\\nu(x)w^j$',
                    '$(1-2xGENVAR+GENVAR^2)^{-\\nu}=\\sum_j C_j^\\nu(x)GENVAR^j$')
main = main.replace('$(1-e^rw)^{-\\nu}(1-e^{-r}w)^{-\\nu}$',
                    '$(1-e^rGENVAR)^{-\\nu}(1-e^{-r}GENVAR)^{-\\nu}$')

# Map the readout and its direction/error coordinates explicitly. Layer weights
# have superscript (L+1), so a transpose must be merged into that superscript.
main = main.replace(r'\dot{\widehat w}_C', r'\dot{\widehat W}_C^{(L+1)}')
main = main.replace(r'\dot{\widehat w}', r'\dot{\widehat W}^{(L+1)}')
main = main.replace(r'\bar u_{w,i}', r'\bar u_{W^{(L+1)},i}')
for a in ['U', 'V', r'\bar u']:
    main = main.replace(a + '_w', a + r'_{W^{(L+1)}}')
main = main.replace('z_w', 'z_{L+1}').replace('B_w', 'B_{L+1}')
main = re.sub(r'(?<![A-Za-z])w_([A-Za-z0-9])', r'W_\1^{(L+1)}', main)
main = re.sub(r'(?<![A-Za-z])w\^\\top', lambda m: r'W^{(L+1)\top}', main)
main = re.sub(r'(?<![A-Za-z])w(?![A-Za-z])', lambda m: r'W^{(L+1)}', main)
main = main.replace('GENVAR', 'w')

# Layer-specific activations retain their layer superscripts; derivative order
# is placed outside parentheses so it cannot be mistaken for a layer number.
activation = re.compile(r"\\phi(?P<pre>'{1,3})?_(?P<idx>\{[^}]+\}|\\[A-Za-z]+|[A-Za-z0-9])"
                        r"(?P<post>'{1,3}|\^\{\([^}]+\)\})?")
def activation_repl(m):
    idx = m['idx'].strip('{}')
    base = r'\phi^{(' + idx + ')}'
    deriv = (m['pre'] or '') + (m['post'] or '')
    return '(' + base + ')' + deriv if deriv else base
main = activation.sub(activation_repl, main)

# Ordinary finite norms have explicit normalization. The signed stability
# lemma's typed sample Hilbert space and the selected M_j spaces remain typed.
main = main.replace('Dense vector norms below are normalized by $\\sqrt n$; selected norms\n'
                    'are specified by their metrics.',
                    'Dense finite vectors use ordinary Euclidean norms, with $1/\\sqrt n$\n'
                    'displayed explicitly. Selected layer norms use the stated metrics $M_j$.')
main = re.sub(r'\\\|((?:(?!\\\|).)+)\\\|_n',
              lambda m: r'\frac{\|' + m[1] + r'\|_2}{\sqrt n}', main)
main = main.replace(r'\langle u,v\rangle_n', r'u^\top v/n')
main = main.replace(r'\|V_na\|', r'\|V_na\|_2/\sqrt n')
main = main.replace(r'\|V_nc_n/\sqrt m\|', r'\|V_nc_n/\sqrt m\|_2/\sqrt n')
main = main.replace(r'\langle W_R^{(L+1)},h_R^{(L)}(v)\rangle',
                    r'\langle W_R^{(L+1)},h_R^{(L)}(v)\rangle_{M_L}')
# Schatten normalization is also displayed, using the ordinary Schatten norm.
main = main.replace('For a rectangular matrix let',
                    'For a rectangular matrix let $\\sigma_i(B)$ be its singular values\n'
                    'and define its ordinary Schatten norm by')
main = main.replace(r'\|B\|_{p,n}=n^{-1/p}(\sum_i\sigma_i(B)^p)^{1/p}',
                    r'\|B\|_{S_p}=(\sum_i\sigma_i(B)^p)^{1/p}')
main = main.replace(r'\|D^2F_a\|_{p,n}', r'\frac{\|D^2F_a\|_{S_p}}{n^{1/p}}')

# Expand only manuscript-local math macros; the chapter has no hidden preamble.
for a, b in {'R': r'\mathbb R', 'E': r'\mathbb E', 'cL': r'\mathcal L',
             'od': r'\mathbin{\odot}', 'dd': r'\,\mathrm d',
             'diag': r'\operatorname{diag}', 'HS': r'\mathrm{HS}',
             'Law': r'\operatorname{Law}'}.items():
    main = re.sub(r'\\' + a + r'(?![A-Za-z])', lambda m, b=b: b, main)
main = braced_macro(main, 'norm', lambda x: r'\left\lVert ' + x + r'\right\rVert')
main = main.replace(r'H\"older', 'Hölder')

# Reflow the few source displays widened by the longer canonical readout and
# activation names. These are line breaks only, with unchanged formulas.
tuple_text = r'(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},W^{(L+1)}/\sqrt n)'
main = main.replace(tuple_text, tuple_text.replace(',', r',\allowbreak '))
def reflow_original_display(marker, substitutions, env='aligned'):
    global main
    pattern = re.compile(r'\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}', re.S)
    matches = [m for m in pattern.finditer(main) if marker in (m[1] or m[2])]
    assert len(matches) == 1, (marker, len(matches))
    m = matches[0]
    body = m[1] or m[2]
    for a, b in substitutions:
        assert a in body, (marker, a)
        body = body.replace(a, b)
    body = '\n' + r'\begin{' + env + '}\n' + body.strip() + '\n' + r'\end{' + env + '}\n'
    replacement = r'\[' + body + r'\]' if m[1] is not None else r'\begin{equation}' + body + r'\end{equation}'
    main = main[:m.start()] + replacement + main[m.end():]

reflow_original_display('t_2=\\max\\{1,\\sup_{j,', [
    ('b=', 'b&='), ('s=', 's&='), ('t_2=', 't_2&='),
    (r'\qquad', r'\\')])
reflow_original_display('z_{a,i}=y_i^\\top h_a^0', [
    ('z_{a,i}=', 'z_{a,i}&='), ('k_{a,i}=', 'k_{a,i}&='), (r'\qquad', r'\\')])
reflow_original_display(r'\lambda=\gamma/m,\qquad', [
    ('\\lambda=', '\\lambda&='), ('H=', 'H&='), ('s=', 's&='), ('b=', 'b&='),
    (r'\qquad', r'\\')])
reflow_original_display(r'\label{cp:selected-readout}', [
    ('Q_C=', 'Q_C&='), (r'\widehat W_C^{(L+1)}=', r'\widehat W_C^{(L+1)}&='),
    ('f_C(v)=', 'f_C(v)&='), (r'\qquad', r'\\')])
reflow_original_display('H_1^c=2b+16s', [
    ('H_1^c=', 'H_1^c&='), ('H_j^c=', 'H_j^c&='), ('H_c=', 'H_c&='),
    ('d_j^c=', 'd_j^c&='), ('F_c=', 'F_c&='), (r'\quad', r'\\')])

# Add labels to the two originally unlabelled local claims so every statement
# and proof has a stable descriptive anchor.
main = main.replace(r'\begin{claim}[Independent fitting and endpoint tails]',
                    r'\begin{claim}[Independent fitting and endpoint tails]' +
                    '\n' + r'\label{cp:selected-fitting}')
main = main.replace(r'\begin{claim}[Finite-horizon comparison]',
                    r'\begin{claim}[Finite-horizon comparison]' +
                    '\n' + r'\label{cp:selected-comparison}')

labels = {}
for m in re.finditer(r'\\begin\{(equation\*?|align\*?|gather\*?)\}(.*?)\\end\{\1\}', main, re.S):
    for key in re.findall(r'\\label\{([^}]+)\}', m[2]):
        labels[key] = 'eq-compression-' + slug(key[3:].removeprefix('eq-'))
for m in re.finditer(r'\\begin\{(' + '|'.join(FORMAL) + r')\}(?:\[([^\]]+)\])?\s*\\label\{([^}]+)\}', main):
    labels[m[3]] = FORMAL[m[1]] + '-compression-' + slug(m[3][3:])
for key in re.findall(r'\\label\{([^}]+)\}', main):
    labels.setdefault(key, 'sec-compression-' + slug(key[3:]))

# Protect all mathematical material, converting each numbered display (and
# each separately labelled row group) into a native Quarto display.
maths = []
def protect(s):
    key = f'@@MATH{len(maths)}@@'
    maths.append(s)
    return key

def display(body, env=None):
    label = re.findall(r'\\label\{([^}]+)\}', body)
    assert len(label) <= 1, label
    body = re.sub(r'\\label\{[^}]+\}', '', body)
    body = body.replace(r'\nonumber', '').strip()
    body = re.sub(r'\n[ \t]*\n', '\n', body)
    if env and env.rstrip('*') in ('align', 'gather'):
        inner = {'align': 'aligned', 'gather': 'gathered'}[env.rstrip('*')]
        body = r'\begin{' + inner + '}\n' + body + '\n' + r'\end{' + inner + '}'
    suffix = ' {#' + labels[label[0]] + '}' if label else ''
    return protect('\n\n$$\n' + body + '\n$$' + suffix + '\n\n')

def display_env(m):
    env, body = m[1], m[2]
    labs = re.findall(r'\\label\{([^}]+)\}', body)
    if len(labs) <= 1:
        return display(body, env)
    # Multiple labelled groups occur only at outer row boundaries. The source
    # group preceding each label is kept intact, including nested gathered rows.
    out = []
    pos = 0
    for lab in re.finditer(r'\\label\{([^}]+)\}', body):
        part = body[pos:lab.end()]
        part = re.sub(r'^\s*\\\\\s*', '', part)
        out.append(display(part, env))
        pos = lab.end()
    assert not body[pos:].strip(), body[pos:]
    return ''.join(out)

main = re.sub(r'\\begin\{(equation\*?|align\*?|gather\*?)\}(.*?)\\end\{\1\}', display_env, main, flags=re.S)
main = re.sub(r'\\\[(.*?)\\\]', lambda m: display(m[1]), main, flags=re.S)
main = re.sub(r'\\\((.*?)\\\)', lambda m: protect('$' + m[1] + '$'), main, flags=re.S)
main = re.sub(r'(?<!\\)\$(.*?)(?<!\\)\$', lambda m: protect('$' + m[1] + '$'), main, flags=re.S)

# Convert the quantitative power table to Markdown, retaining every entry.
table = re.compile(r'\\begin\{center\}\\small\s*\\begin\{tabular\}\{c\|c\|c\}(.*?)\\end\{tabular\}\\end\{center\}', re.S)
def table_repl(m):
    rows = m[1].replace(r'\hline', '').strip().split(r'\\')
    parsed = ['| ' + ' | '.join(x.strip() for x in row.split('&')) + ' |' for row in rows if row.strip()]
    return '\n\n' + '\n'.join(parsed[:1] + ['|---|---|---|'] + parsed[1:]) + '\n\n'
main = table.sub(table_repl, main)

# Keep the source's roman-part markers as titled paragraphs. This preserves
# references to (i) and (iii), including the intervening display equations.
main = re.sub(r'\\begin\{enumerate\}(?:\[[^\n]*\])?', '\n', main)
main = main.replace(r'\end{enumerate}', '\n')
for number in ['i', 'ii', 'iii']:
    main = main.replace(r'\item ', '\n**(' + number + ')** ', 1)

# Convert formal environments with long outer fences and shorter inner fences.
# This preserves nested claim/proof structure in both Pandoc and Quarto.
token = re.compile(r'\\(?P<kind>begin|end)\{(?P<env>' + '|'.join(FORMAL) + r'|proof)\}'
                   r'(?:\[(?P<title>[^\]]+)\])?(?:\s*\\label\{(?P<label>[^}]+)\})?')
stack = []
last_statement = None
proof_counts = Counter()
formal_counts = Counter()
def formal_repl(m):
    global last_statement
    env = m['env']
    if m['kind'] == 'end':
        old, fence = stack.pop()
        assert old == env, (old, env)
        return '\n\n' + fence + '\n\n'
    fence = ':' * (15 - 2 * len(stack))
    assert len(fence) >= 3
    stack.append((env, fence))
    formal_counts[env] += 1
    title = m['title']
    if env == 'proof':
        anchorbase = (last_statement or 'sec-compression-setup').split('-compression-', 1)[-1]
        if title and 'Verification of the working whole-sphere' in title:
            anchorbase = 'source-whole-sphere-verification'
        elif title and r'\Cref{cp:headline}' in title:
            anchorbase = 'headline'
        proof_counts[anchorbase] += 1
        if proof_counts[anchorbase] > 1:
            anchorbase += '-' + str(proof_counts[anchorbase])
        return ('\n\n[]{#proof-compression-' + anchorbase + '}\n\n' + fence + ' {.proof}'
                + '\n\n' + (('**' + title + '.**\n\n') if title else ''))
    assert m['label'], m.group(0)
    last_statement = labels[m['label']]
    return '\n\n' + fence + ' {#' + last_statement + '}\n\n' + (('### ' + title + '\n\n') if title else '')
main = token.sub(formal_repl, main)
assert not stack

# Sections and subsection anchors are native Quarto identifiers. Paragraphs
# inside proofs become titled prose with an anchor, never new numbered chapters.
heading = re.compile(r'\\(?P<kind>section|subsection|paragraph)\{(?P<title>[^}]+)\}'
                     r'(?:\s*\\label\{(?P<label>[^}]+)\})?')
heading_counts = Counter()
def heading_repl(m):
    title = m['title'].rstrip('.')
    label = labels[m['label']] if m['label'] else 'sec-compression-' + slug(title)
    heading_counts[label] += 1
    assert heading_counts[label] == 1, label
    if m['kind'] == 'paragraph':
        return '\n\n[' + title + '.]{#' + label + '}\n\n'
    return '\n\n' + ('## ' if m['kind'] == 'section' else '### ') + title + ' {#' + label + '}\n\n'
main = heading.sub(heading_repl, main)
main = main.replace(r'\noindent', '')
main = braced_macro(main, 'textbf', lambda x: '**' + x + '**')
main = braced_macro(main, 'emph', lambda x: '*' + x + '*')
main = main.replace(r'\quad', ' ')
main = main.replace('~', ' ')

# Restore math and translate every source cross-reference. References in proof
# titles and prose use the same native identifiers as statements and equations.
main = re.sub(r'@@MATH(\d+)@@', lambda m: maths[int(m[1])], main)
main = re.sub(r'(?:Lemma|Claim|Theorem|Proposition|Section)\s*\\ref\{([^}]+)\}', lambda m: '@' + labels[m[1]], main)
main = re.sub(r'\\(?:Cref|cref|ref|eqref)\{([^}]+)\}',
              lambda m: ' and '.join('@' + labels[x] for x in m[1].split(',')), main)
main = re.sub(r'(@[a-z][a-z0-9-]+)--(@[a-z])', r'\1 through \2', main)
main = re.sub(r'\n{3,}', '\n\n', main).strip()

lead = '''# Complete-trajectory compression {#ch-trajectory-compression}

This chapter constructs three autonomous approximations to finite-width,
Gaussian-initialized deep nonlinear gradient flow. Their error is negligible
relative to the variability between independent dense runs, uniformly over
the promised input domain and the entire physical training trajectory,
including its fitted limit. Legendre retains $n^{5/4+o(1)}$ moving coordinates
and fixed dense mixers. Harmonic retains $O((\\log n)^{3d+2})$ total real
coordinates for the whole input sphere. Taylor retains $O((\\log n)^3$)
coordinates for a fixed input panel declared before initialization.

These results use a fixed dataset, fixed depth, a positive population feature
Gram gap, and an explicit small-label condition. They compare finite neural
systems and do not assert a population limit, a raw-GD approximation, a
finite-precision guarantee, or efficient preprocessing. The selected
constructions also attain absolute error $Y/n$. Their theoretical compilers
use initialization derivatives; empirical rollout-based implementations have
a different setup contract.

The layer convention agrees with @sec-docs-notation-l1: the stored readout is
$W^{(L+1)}$ and the activation in hidden layer $\\ell$ is $\\phi^{(\\ell)}$.
The initialization here sets $W^{(L+1)}(0)=0$ exactly, which is a separately
stated model from the book's finite small-Gaussian-readout convention.
'''
lead = lead.replace('$O((\\log n)^3$)', '$O((\\log n)^3)$')
out = lead + '\n' + main + '\n'
# The maintained edition disables section numbering; name section links explicitly.
out = out.replace('@sec-docs-notation-l1', '[the shared notation contract](notation.qmd#sec-docs-notation-l1)')
out = out.replace('@sec-compression-setup', '[the setup](#sec-compression-setup)')
assert r'\label{' not in out
assert r'\input{' not in out
assert not re.search(r'\\(?:begin|end)\{(?:' + '|'.join(FORMAL) + r'|proof|enumerate|center|tabular)\}', out)
assert not re.search(r'\\(?:Cref|ref|eqref)\{', out)
identifiers = re.findall(r'\{#([a-z0-9-]+)', out)
assert len(identifiers) == len(set(identifiers)), Counter(identifiers)
references = set(re.findall(r'@((?:sec|eq|thm|lem|prp|cor|def|rem)-[a-z0-9-]+)', out))
assert references <= set(identifiers) | {'sec-docs-notation-l1'}, references - set(identifiers)
(HERE/'promotion_compression.qmd').write_text(out)
SCRATCH.mkdir(parents=True, exist_ok=True)
(SCRATCH/'source_label_mapping.json').write_text(json.dumps(labels, indent=2) + '\n')
inventory = {
    'inputs': {f: {'lines': len(raw[f].splitlines()),
                   'sha256': hashlib.sha256(raw[f].encode()).hexdigest()} for f in INPUTS},
    'source_labels': len(re.findall(r'\\label\{', ''.join(raw.values()))),
    'candidate_source_and_added_labels': len(labels),
    'formal_environments': dict(formal_counts),
    'proof_anchors': sum(proof_counts.values()),
    'total_identifiers': len(identifiers),
    'equation_identifiers': sum(x.startswith('eq-') for x in identifiers),
    'unresolved_local_references': [],
    'candidate_lines': len(out.splitlines()),
    'candidate_sha256': hashlib.sha256(out.encode()).hexdigest(),
    'omissions': ['manuscript preamble, title/author/date and abstract wrapper',
                  'global symbol-count bookkeeping table and its accompanying prose'],
    'notation_changes': ['finite readout w -> W^{(L+1)}',
                         'layer activation phi_j -> phi^{(j)}',
                         'dense normalized norms and pairings expanded explicitly',
                         'claims use native lemma divisions; inline verifications use proof divisions'],
}
(SCRATCH/'conversion_inventory.json').write_text(json.dumps(inventory, indent=2) + '\n')
print(json.dumps(inventory, indent=2))
