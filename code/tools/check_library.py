"""Check the self-contained source-library boundary and Markdown file links.

This is a structural check, not a mathematical proof verifier. It runs without
loading implementation modules and does not inspect historical research files.
"""

import ast
from pathlib import Path
import re
import sys


def prose_only(text: str) -> str:
    """Ignore code and displayed/inline math before scanning Markdown links."""
    text = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", text, flags=re.M | re.S)
    text = re.sub(r"^~~~[^\n]*\n.*?^~~~[^\n]*$", "", text, flags=re.M | re.S)
    text = re.sub(r"\\\[.*?\\\]", "", text, flags=re.S)
    text = re.sub(r"\\\(.*?\\\)", "", text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)
    text = re.sub(r"(?<!\\)\$[^$\n]*?(?<!\\)\$", "", text)
    return re.sub(r"`+[^`\n]*`+", "", text)


def main(root=None) -> int:
    root = Path(root).resolve() if root is not None else Path(__file__).resolve().parents[2]
    allowed_roots = (root / "docs", root / "code")
    errors = []
    count = 0
    for directory in allowed_roots:
        if not directory.is_dir():
            errors.append(f"missing library directory: {directory.name}")
            continue
        for source in sorted(directory.rglob("*")):
            if source.is_symlink():
                errors.append(f"symbolic link in source library: {source.relative_to(root)}")
                continue
            if not source.is_file() or source.suffix not in (".md", ".py"):
                continue
            count += 1
            text = source.read_text(encoding="utf-8")
            if source.suffix == ".md":
                prose = prose_only(text)
                targets = [m.group(2) for m in re.finditer(r"\]\((<?)([^)\n]+?)(>?)\)", prose)]
                targets += [m.group(1) for m in re.finditer(
                    r"^\s{0,3}\[[^\]\n]+\]:\s*<?([^\s>]+)>?", prose, re.M)]
                for target in targets:
                    if target.startswith(("https://", "http://", "mailto:", "#")):
                        continue
                    target = re.sub(r":\d+(?=#|$)", "", target).split("#", 1)[0]
                    if not target:
                        continue
                    linked = (source.parent / target).resolve()
                    if Path(target).is_absolute() or not any(
                        linked.is_relative_to(base) for base in allowed_roots
                    ):
                        errors.append(f"external local dependency: {source.relative_to(root)} -> {target}")
                    elif not linked.exists():
                        errors.append(f"broken library link: {source.relative_to(root)} -> {target}")
            else:
                try:
                    tree = ast.parse(text, filename=str(source))
                except SyntaxError as error:
                    errors.append(str(error))
                    continue
                for node in ast.walk(tree):
                    imports = []
                    if isinstance(node, ast.Import):
                        imports = [alias.name.split(".")[0] for alias in node.names]
                    elif isinstance(node, ast.ImportFrom) and not node.level and node.module:
                        imports = [node.module.split(".")[0]]
                    for name in imports:
                        if name not in sys.stdlib_module_names and name not in {"numpy", "pde"}:
                            errors.append(f"undeclared import: {source.relative_to(root)}: {name}")
                    modules = []
                    if isinstance(node, ast.Import):
                        modules = [(root / "code", alias.name) for alias in node.names
                                   if alias.name.split(".")[0] == "pde"]
                    elif isinstance(node, ast.ImportFrom):
                        if node.level:
                            base = source.parent
                            for _ in range(node.level - 1):
                                base = base.parent
                            modules = [(base, node.module or "")]
                        elif node.module and node.module.split(".")[0] == "pde":
                            modules = [(root / "code", node.module)]
                    for base, module in modules:
                        target = base.joinpath(*module.split(".")).resolve()
                        if not target.is_relative_to(root / "code") or not (
                            target.with_suffix(".py").is_file() or (target / "__init__.py").is_file()
                        ):
                            errors.append(f"missing local import: {source.relative_to(root)}: {module}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Library boundary and local links checked: {count} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
