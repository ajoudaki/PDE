"""One reproducible editorial rearrangement; no scientific text generation."""
from collections import Counter, defaultdict
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
BASE = 'af9ee2765187a9d53539b60e81575a7c02d252a5'
OUT = ROOT / 'data/generated/mfp_book_reorganization_20261010'
C2 = 'docs/02-gaussian-reuse.qmd'
C7 = 'docs/07-observable-closure.qmd'
C8 = 'docs/08-autonomous-computation.qmd'
PREFIX = 'sec-docs-gaussian-calculus-l'
ID = re.compile(r'\{[^}\n]*?(?<!\\)#([A-Za-z][\w:.-]*)[^}\n]*\}')
LINK = re.compile(r'(?P<start>\]\()(?P<file>[^\s)#]*\.qmd)?#(?P<id>[\w:.-]+)(?P<end>\))')
REF = re.compile(r'(?<!\w)@((?:sec|eq|thm|lem|prp|cor|def|rem|fig|tbl|ch)-[\w-]+)')


def baseline(path):
    return subprocess.check_output(['git', 'show', f'{BASE}:{path}'], cwd=ROOT).decode()


def heading_position(text, number):
    pattern = rf'^#+ [^\n]*\{{#{PREFIX}{number}\}}[^\n]*\n'
    matches = list(re.finditer(pattern, text, re.M))
    assert len(matches) == 1, (number, len(matches))
    return matches[0].start()


def adjust_heading(text, number, level):
    return re.sub(rf'^#+ (?=[^\n]*\{{#{PREFIX}{number}\}})', '#' * level + ' ', text, flags=re.M)


def normalized(text):
    # Heading hierarchy and chapter paths are editorial; retain titles and IDs.
    text = re.sub(r'^#{1,6} ', '# ', text, flags=re.M)
    text = LINK.sub(lambda m: '](' + '#' + m['id'] + ')', text)
    return Counter(line for line in text.splitlines() if line.strip())


def reorganize():
    paths = sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'docs').glob('*.qmd'))
    original = {p: baseline(p) for p in paths}
    expected = original.copy()
    edited = original.copy()
    moves = []
    intervals = [(1824, 2156), (2165, 2248), (4918, 5259), (5338, 5637), (3305, 3672)]
    chunks = []
    for start, end in intervals:
        a, b = heading_position(original[C7], start), heading_position(original[C7], end)
        text = original[C7][a:b]
        chunks.append(text)
        edited[C7] = edited[C7].replace(text, '', 1)
        moves.append(dict(source=C7, destination=C2, start=PREFIX+str(start),
                          stop_before=PREFIX+str(end), lines=text.count('\n'),
                          sha256=hashlib.sha256(text.encode()).hexdigest()))
    # The forest subsection becomes a sibling of the moving-flow recurrence.
    chunks[1] = adjust_heading(chunks[1], 2165, 3)
    pos = heading_position(edited[C2], 263)
    edited[C2] = edited[C2][:pos] + ''.join(chunks) + edited[C2][pos:]
    # Width identification now follows the finite calculus at section level.
    a = heading_position(edited[C2], 263)
    b = edited[C2].index('## A. Contained probability', a)
    width = edited[C2][a:b]
    width = adjust_heading(width, 263, 2)
    width = re.sub(r'^(#{4,6}) ', lambda m: m[1][1:] + ' ', width, flags=re.M)
    edited[C2] = edited[C2][:a] + width + edited[C2][b:]
    for number, level in [(2156, 2), (2248, 3), (2397, 3), (5259, 2), (5637, 2), (5840, 2)]:
        edited[C7] = adjust_heading(edited[C7], number, level)

    replacements = []

    def replace(path, old, new, source=None):
        source = source or path
        assert edited[path].count(old) == 1, (path, old[:100], edited[path].count(old))
        assert expected[source].count(old) == 1, (source, old[:100], 'baseline')
        edited[path] = edited[path].replace(old, new, 1)
        expected[source] = expected[source].replace(old, new, 1)
        replacements.append(dict(path=path, original_path=source, old=old, new=new))

    title = 'Mean-Field Peeling: A Gaussian Calculus for Deep Networks'
    replace(C2, '2. Gaussian calculus for reused matrices', '2. ' + title)
    replace('docs/index.qmd', '[Gaussian calculus for reused matrices]', '[' + title + ']')
    replace(C2,
        'A population description must retain the joint dependence created by forward, backward and adaptive reuse of the same matrices. The chapter develops conditioning, fixed-program laws, source-response formulas, trained matrix memories, adaptive transcripts and filtering in one place.',
        'Mean-field peeling (MFP) organizes the reduction of neural-network derivative contractions and finite Gaussian programs to explicit Gaussian calculations while retaining forward/backward matrix reuse. This chapter brings together its established finite calculus, worked constructions and width-identification arguments. Each result retains its own architecture, regularity, initialization and limiting assumptions.\n\n'
        'The route through the method is [Gaussian conditioning](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l105), [moving-flow derivative recurrences and forest factorization](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l1824), [contraction trees, Gaussian evaluation and observable heads](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l4918), [finite loss-GD pullbacks](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l3305), and [fixed-program width identification](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l263). The later sections extend the conditioning machinery to trained memories and adaptive source programs.\n\n'
        'Finite derivatives and Gaussian expectations are distinct from integration along a training trajectory. These scoped results do not assert a general observable-grammar theorem or convergence of an infinite training-time Taylor series. [Chapter 7](07-observable-closure.qmd#ch-observable-closure) treats closure and approximation boundaries; [Chapter 8](08-autonomous-computation.qmd#ch-autonomous-computation) supplies quantitative refinement and convergent autonomous computation.')
    old_intro = original[C2].split('This chapter develops Gaussian matrix reuse', 1)[1].split('### 1. One forward call', 1)[0]
    replace(C2, 'This chapter develops Gaussian matrix reuse' + old_intro,
        'Use [the shared notation](notation.qmd#sec-docs-notation-l1). We begin with exact Gaussian conditioning and finite derivative identities; the later width-limit statements supply their separate probabilistic hypotheses.\n\n')
    replace(C7,
        'Suitable current observables can retain the information needed for prediction and support autonomous finite approximations. The chapter moves from information constraints and exact observable calculus through scoped obstructions to a sufficient hierarchy and concrete initialized constructions.',
        'Suitable current observables can retain the information needed for prediction and support autonomous finite approximations. The chapter moves from information constraints and scoped approximation obstructions to a sufficient hierarchy and concrete initialized constructions. Its finite derivative and Gaussian calculations are developed together in [Mean-Field Peeling](02-gaussian-reuse.qmd#ch-gaussian-reuse).')
    replace(C7, '7.2. Forest factorization and small exact certificates', '7.2. A quadratic initialization-jet certificate')
    replace(C2, '7. Reusable finite calculus and exact certificates',
        '7. Reusable finite calculus and forest factorization', source=C7)
    replace(C7, 'No retained table is an input to these operations.\n',
        'No retained table is an input to these operations. The [decorated-forest factorization and canonical keys](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l2165) are developed in the MFP chapter.\n')
    replace(C7,
        'Here is the expectation argument, also proved in [Section 7.2](07-observable-closure.qmd#sec-docs-gaussian-calculus-l2156).',
        'Here is the expectation argument, also proved in [the decorated-forest factorization](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l2165).')
    replace(C7, 'finite loss program, as proved above; only then does $N\\to\\infty$.',
        'finite loss program, as proved in [the quadratic physical-loss width theorem](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l5187); only then does $N\\to\\infty$.')
    replace(C7, 'Set $c=1/\\sqrt3$. For every $T>0$, $0<\\delta<1$, and',
        'Use the quadratic model and deterministic raw-GD output limits $F_k^\\eta$ from [the quadratic physical-loss width theorem](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l5187), with $c=1/\\sqrt3$. For every $T>0$, $0<\\delta<1$, and')
    replace(C7, 'then evaluate by $m(p)m(q)$ from B.',
        'then evaluate by $m(p)m(q)$ from [Gaussian forest evaluation](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l4967).')
    for old, new in [
        ('parameter-contraction trees from A.', 'parameter-contraction trees from [A](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l4923).'),
        ('leading value from B when omitted.', 'leading value from [B](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l4967) when omitted.'),
        ('finite derivative polynomial from C,', 'finite derivative polynomial from [C](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l5064),'),
        ('one lower order from E and', 'one lower order from [E](02-gaussian-reuse.qmd#sec-docs-gaussian-calculus-l5338) and')]:
        replace(C7, old, new)
    replace(C2,
        'The exact integrated-query memories called [Section 13](02-gaussian-reuse.qmd#sec-docs-finite-optimization-and-controls-l2167) in these fragments\nare proved in [finite controls](09-trainability.qmd#sec-docs-finite-optimization-and-controls-l1).\nThat chapter also contains the associated response and physical-control\nfragments S, I, C and E.',
        'The exact integrated-query memories used here are proved in [Section 13 above](02-gaussian-reuse.qmd#sec-docs-finite-optimization-and-controls-l2167).\nThe [finite controls](09-trainability.qmd#sec-docs-finite-optimization-and-controls-l1) material contains the associated response and physical-control\nfragments S, I, C and E.')
    # Existing semantic mislinks exposed at the boundary: quoted lemma title
    # and Gaussian net inequality identify the correct unchanged source.
    replace(C8,
        'The maintained dependency for the Gaussian identification is [Section 9](07-observable-closure.qmd#sec-docs-gaussian-calculus-l3305),\n“A Gaussian source lemma with contained norm and Wick proofs,” in the\nobservable-closure chapter.',
        'The maintained dependency for the Gaussian identification is [A Gaussian source lemma with contained norm and Wick proofs](09-trainability.qmd#sec-docs-linear-dynamics-l1734), in the\ntrainability chapter.')
    replace(C8,
        'Gaussian net argument in [Section 9](07-observable-closure.qmd#sec-docs-gaussian-calculus-l3305) of the observable-closure chapter,',
        'Gaussian net argument in [the Gaussian source lemma](09-trainability.qmd#sec-docs-linear-dynamics-l1734) of the trainability chapter,')

    owners = {}
    for path, text in edited.items():
        for ident in ID.findall(text):
            assert ident not in owners, ('duplicate', ident)
            owners[ident] = path
    rewrites = []
    for path, text in edited.items():
        def relink(match):
            target = owners.get(match['id'])
            assert target, ('missing', path, match['id'])
            destination = Path(target).name
            old_file = match['file']
            if not old_file and target == path:
                return match[0]
            if old_file != destination:
                rewrites.append(dict(source=path, target=match['id'], before=old_file, after=destination))
            return '](' + destination + '#' + match['id'] + ')'
        edited[path] = LINK.sub(relink, text)

    # Whole-source conservation, with exactly enumerated editorial exceptions.
    assert sum((normalized(t) for t in expected.values()), Counter()) == sum((normalized(t) for t in edited.values()), Counter())
    math = lambda book: Counter(m for t in book.values() for m in re.findall(r'^\$\$\n.*?^\$\$', t, re.M | re.S))
    assert math(original) == math(edited), 'display mathematics changed'
    assert Counter(i for t in original.values() for i in ID.findall(t)) == Counter(owners.keys()), 'identifier inventory changed'
    assert Counter(r for t in original.values() for r in REF.findall(t)) == Counter(r for t in edited.values() for r in REF.findall(t)), 'native references changed'
    missing = [(p, r) for p, t in edited.items() for r in REF.findall(t) if r not in owners]
    assert not missing, missing
    report = dict(base_commit=BASE, moved_sections=moves, moved_lines=sum(m['lines'] for m in moves),
                  editorial_replacements=replacements, link_rewrites=rewrites, identifiers=len(owners),
                  display_math_blocks=sum(math(original).values()),
                  checks='PASS: whole-book line conservation modulo listed editorial changes; exact display mathematics, IDs and native references preserved; all book reference destinations resolve')
    return original, edited, report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--check-render', action='store_true')
    args = parser.parse_args()
    original, edited, report = reorganize()
    changes = []
    for path, text in edited.items():
        current = (ROOT / path).read_text()
        assert current in (original[path], text), ('concurrent changes', path)
        if original[path] != text:
            changes.append(path)
        if args.apply and current != text:
            (ROOT / path).write_text(text)
        elif not args.apply:
            assert current == text, ('not yet applied', path)
    report['changed_paths'] = changes
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'preservation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['moved_lines', 'identifiers', 'display_math_blocks', 'changed_paths', 'checks']}, indent=2))
    if args.check_render:
        check_render(edited)


def check_render(book):
    output = OUT / 'build/html'

    class Page(HTMLParser):
        def __init__(self, path):
            super().__init__(convert_charrefs=True)
            self.ids, self.links = Counter(), []
            self.feed(path.read_text())

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if 'id' in attrs:
                self.ids[attrs['id']] += 1
            if tag == 'a' and attrs.get('href'):
                self.links.append(attrs['href'])

    pages = {p.name: Page(p) for p in output.glob('*.html')}
    errors, count, fragments = [], 0, 0
    for name, source in book.items():
        page = pages[Path(name).with_suffix('.html').name]
        for ident in ID.findall(source):
            count += 1
            if page.ids[ident] != 1:
                errors.append(f'{name}: ID {ident} count={page.ids[ident]}')
    for name, page in pages.items():
        for href in page.links:
            uri = urlsplit(href)
            if uri.scheme or uri.netloc:
                continue
            target = (output / unquote(uri.path)).resolve() if uri.path else output / name
            if not target.exists():
                errors.append(f'{name}: missing {href}')
            elif uri.fragment and target.suffix == '.html' and target.parent == output:
                fragments += 1
                if unquote(uri.fragment) not in pages[target.name].ids:
                    errors.append(f'{name}: missing fragment {href}')
    report = dict(pages=len(pages), source_targets=count, local_fragment_links=fragments, errors=errors)
    (OUT / 'build/html_checks.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    assert not errors, errors


if __name__ == '__main__':
    main()
