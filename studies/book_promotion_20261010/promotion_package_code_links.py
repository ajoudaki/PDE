"""Package linked repository code beside HTML, PDF and editable LaTeX exports."""
from __future__ import annotations

import html
import os
from pathlib import Path
import re
import shutil
from urllib.parse import quote, unquote, urlsplit, urlunsplit


def package(output: Path, code: Path) -> int:
    output, code = output.resolve(), code.resolve()
    count = 0
    for page in output.rglob('*.html'):
        # Bundled source HTML is not a rendered book page.
        if any(name in ('code', 'docs') for name in page.relative_to(output).parts[:-1]):
            continue

        def replace(match):
            nonlocal count
            uri = urlsplit(html.unescape(match[2]))
            relative = Path(unquote(uri.path[len('../code/'):]))
            source = (code/relative).resolve()
            if not source.is_relative_to(code) or not source.is_file():
                raise ValueError(f'Missing or unsafe code resource: {match[2]}')
            target = output/'code'/source.relative_to(code)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            path = quote(Path(os.path.relpath(target, page.parent)).as_posix())
            link = html.escape(urlunsplit(('', '', path, uri.query, uri.fragment)), quote=True)
            count += 1
            return 'href='+match[1]+link+match[1]

        original = page.read_text(encoding='utf-8')
        rewritten = re.sub(r'''\bhref=(["'])(\.\./code/[^"']+)\1''', replace, original)
        if rewritten != original:
            page.write_text(rewritten, encoding='utf-8')
    return count


def package_source_bundle(output: Path, project: Path, code: Path) -> None:
    # Linked Markdown guides have further relative links into docs/ and code/.
    # Preserve that complete source layout instead of chasing selected links.
    parents = {output}
    parents.update(p.parent for suffix in ('*.pdf', '*.tex')
                   for p in output.rglob(suffix)
                   if not p.is_relative_to(output/'code') and
                   not p.is_relative_to(output/'docs'))
    for source_root in (project, code):
        sources = []
        for directory, dirs, files in os.walk(source_root):
            dirs[:] = [d for d in dirs if not d.startswith(('.', '_book', '_site'))
                       and d not in ('__pycache__', 'node_modules')
                       and (Path(directory)/d).resolve() != output.resolve()]
            sources.extend(Path(directory)/name for name in files
                           if not name.startswith('.') and not name.endswith(('.pyc', '.pyo')))
        for source in sources:
            if not source.resolve().is_relative_to(source_root.resolve()):
                raise ValueError(f'Unsafe source-bundle path: {source}')
            for parent in parents:
                target = parent/source_root.name/source.relative_to(source_root)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)


if __name__ == '__main__':
    project = Path(os.environ['QUARTO_PROJECT_DIR']).resolve()
    output = Path(os.environ['QUARTO_PROJECT_OUTPUT_DIR'])
    if not output.is_absolute():
        output = project/output
    if output.resolve() == project:
        raise ValueError('Packaging requires a separate output directory')
    code = (project.parent/'code').resolve()
    count = package(output, code)
    package_source_bundle(output, project, code)
    print(f'Packaged source docs/code bundle; rewrote {count} HTML code links.')
