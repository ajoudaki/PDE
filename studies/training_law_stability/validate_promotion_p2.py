"""Validate/assemble the frozen proof-only P2 edition without a repository import."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    inputs = args.inputs.resolve()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    manifest = json.loads((inputs / 'P2_MANIFEST.json').read_text())
    checks = []
    for name, expected in manifest['inputs'].items():
        assert digest(inputs / name) == expected, name
    checks.append('All seven frozen edition/baseline/dependency input hashes match.')

    baseline = (inputs / 'P2_GLOBAL_BASELINE.md').read_text()
    assembled = baseline
    for edit in json.loads((inputs / 'P2_GLOBAL_EDITS.json').read_text()):
        assert assembled.count(edit['old']) == 1, edit['old'][:60]
        assembled = assembled.replace(edit['old'], edit['new'])
    addition = (inputs / 'P2_ADDITION.md').read_text()
    assembled = assembled.rstrip() + '\n\n' + addition
    assert assembled == (inputs / 'P2_GLOBAL_EDITION.md').read_text()
    checks.append('Edition equals exactly the five declared scope edits plus C.4; all other chapter text is preserved.')

    # The addition contains every new argument and only canonical references.
    for forbidden in ['studies/', 'data/generated/', '/root', 'R1_', 'P2_']:
        assert forbidden not in addition, forbidden
    for text in [addition, (inputs / 'P2_DEPENDENCIES.md').read_text()]:
        assert text.count('\\[') == text.count('\\]')
        stack = []
        for kind, environment in re.findall(r'\\(begin|end)\{([^}]+)\}', text):
            if kind == 'begin':
                stack.append(environment)
            else:
                assert stack and stack.pop() == environment, environment
        assert not stack
    tags = set(re.findall(r'\\tag\{((?:T|P|A)\d+[a-z]?)\}', addition))
    refs = set(re.findall(r'\(((?:T|P|A)\d+[a-z]?)\)', addition))
    assert refs <= tags, sorted(refs - tags)
    checks.append('New proof has no study/runtime dependencies, balanced display environments, and no missing T/P/A equation references.')

    dep = (inputs / 'P2_DEPENDENCIES.md').read_text()
    excerpts = {}
    marker = r'<!-- Verbatim source: (.*?) lines (\d+)–(\d+) -->\n\n'
    matches = list(re.finditer(marker, dep))
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(dep)
        excerpts[(match[1], int(match[2]), int(match[3]))] = dep[match.end():end].rstrip() + '\n'
    docs = output / 'docs'
    docs.mkdir()
    (docs / 'global_nonlinear.md').write_text(assembled)
    (docs / 'README.md').write_bytes((inputs / 'P2_DOCS_README.md').read_bytes())
    (docs / 'NOTATION.md').write_text(excerpts[('docs/NOTATION.md', 1, 98)])
    (docs / 'special_data_limits.md').write_text(excerpts[('docs/special_data_limits.md', 3785, 4200)])
    (docs / 'finite_dynamics.md').write_text(excerpts[('docs/finite_dynamics.md', 1, 227)])
    (output / 'standalone_proof.md').write_text(addition + '\n\n' + dep)

    # Validate precisely the new guide link and all links in the new subsection.
    def anchor(heading):
        return re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
    def check_link(target):
        file, _, fragment = target.partition('#')
        dest = docs / (file or 'global_nonlinear.md')
        assert dest.is_file(), target
        if fragment:
            headings = re.findall(r'^#{1,6} (.+)$', dest.read_text(), re.M)
            assert fragment in {anchor(h) for h in headings}, target
    for target in re.findall(r'\]\(([^)]+)\)', addition):
        check_link(target)
    new_guide = (inputs / 'P2_DOCS_README.md').read_text()
    old_guide = (inputs / 'P2_README_BASELINE.md').read_text()
    old_links = set(re.findall(r'\]\(([^)]+)\)', old_guide))
    for target in set(re.findall(r'\]\(([^)]+)\)', new_guide)) - old_links:
        check_link(target)
    checks.append('All links in the new subsection and the new guide link resolve in the standalone edition, including C.4 and Gaussian foundation fragments.')

    results = {
        'python': sys.version,
        'inputs_directory': str(inputs),
        'output_directory': str(output),
        'checks': checks,
        'output_sha256': {str(p.relative_to(output)): digest(p)
                          for p in sorted(output.rglob('*')) if p.is_file()},
        'scope': 'Proof-only edition validation; no empirical claim, training experiment, maintained API, or whole-book export test.',
        'unread_unvalidated_complement': 'Unchanged chapters/guide links and unrelated code/exporter are outside this check.',
    }
    (output / 'validation.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
