"""Standalone, read-only-source PDF exporter for the maintained PDE book.

No repository tools are executed. All conversion and LaTeX work happens in a
fresh private directory; only a checked PDF and its receipt are published.
"""
from pathlib import Path
import argparse
from datetime import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

BUNDLE = Path(__file__).resolve().parent
ARCHIVE_HASH = "5def6e1ff535e397becce292ee97767a947306150b9fb1488003b67ac3417c5e"
DEFAULT_REPO = BUNDLE.parents[2]
DEFAULT_OUTPUT = Path("/tmp/PDE-book-latest.pdf")
DEFAULT_ARCHIVE = Path.home() / ".cache/pde-book-pdf/pandoc-3.6.4-linux-amd64.tar.gz"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def discover(repo):
    """Guide-link order first; include and announce other maintained Markdown."""
    guide = repo / "docs/README.md"
    if not guide.is_file():
        raise ValueError(f"Missing book introduction: {guide}")
    available = {p.relative_to(repo).as_posix() for p in (repo / "docs").rglob("*.md") if p.is_file()}
    for name in available:
        if not (repo / name).resolve().is_relative_to(repo):
            raise ValueError(f"Source symlink leaves the repository: {name}")
    order = ["docs/README.md"]
    if "docs/NOTATION.md" in available:
        order.append("docs/NOTATION.md")
    guide_text = guide.read_text(encoding="utf-8")
    for destination in re.findall(r"\[[^\]]*\]\(([^)]+)\)", guide_text):
        parsed = urlsplit(destination.strip().strip("<>"))
        if parsed.scheme or not parsed.path:
            continue
        candidate = (guide.parent / unquote(parsed.path)).resolve()
        if candidate.is_relative_to(repo):
            name = candidate.relative_to(repo).as_posix()
            if name in available and name not in order:
                order.append(name)
    unlisted = sorted(available.difference(order))
    order.extend(unlisted)
    if (repo / "code/README.md").is_file():
        if not (repo / "code/README.md").resolve().is_relative_to(repo):
            raise ValueError("Implementation-guide symlink leaves the repository")
        order.append("code/README.md")
    chapter = 0
    files = []
    for name in order:
        if name == "docs/README.md":
            label = "Introduction"
        elif name == "docs/NOTATION.md":
            label = "Notation"
        elif name == "code/README.md":
            label = "Appendix"
        else:
            chapter += 1
            label = str(chapter)
        files.append([name, label])
    return files, unlisted


def snapshot(repo, work):
    # Retry a concurrently edited book; do not lock, alter, or revert it.
    for attempt in range(3):
        files, unlisted = discover(repo)
        try:
            payload = {name: (repo / name).read_bytes() for name, _ in files}
            if files != discover(repo)[0]:
                continue
            if any((repo / name).read_bytes() != data for name, data in payload.items()):
                continue
        except FileNotFoundError:
            continue
        for name, data in payload.items():
            target = work / "snapshot" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        return files, unlisted, payload
    raise RuntimeError("The book kept changing during snapshot capture. Please retry shortly; nothing was locked or modified.")


def validate_output(repo, output):
    if output.suffix.lower() != ".pdf":
        raise ValueError("The output filename must end in .pdf")
    if output.is_relative_to(repo):
        raise ValueError("Choose an output outside the repository; this exporter deliberately never writes inside it.")
    if output.exists() and not output.is_file():
        raise ValueError(f"Output is not a regular file: {output}")


def run(command, work, name):
    result = subprocess.run(command, cwd=work, capture_output=True, text=True, errors="replace", timeout=300)
    transcript = result.stdout + "\n" + result.stderr
    (work / name).write_text(transcript)
    if result.returncode:
        raise RuntimeError(f"{Path(command[0]).name} failed; see {work / name}\n{transcript[-2500:]}")
    return result.stdout


def install_private_converter(work, archive=None):
    """Use pinned installed Pandoc, or verify an external release archive."""
    if archive is None:
        installed = shutil.which("pandoc")
        if installed:
            version = run([installed, "--version"], work, "pandoc-version.txt").splitlines()
            if not version or version[0].strip() != "pandoc 3.6.4":
                raise RuntimeError("This exporter requires Pandoc 3.6.4. Use --pandoc-archive to supply its verified release archive instead of the installed version.")
            (work / "pandoc").symlink_to(Path(installed).resolve())
            return
        archive = DEFAULT_ARCHIVE
    archive = archive.expanduser().resolve()
    if not archive.is_file():
        raise RuntimeError(f"Pandoc 3.6.4 is not available. Install it on PATH or supply --pandoc-archive PATH. Expected cache: {DEFAULT_ARCHIVE}. See code/tools/book_pdf/README.md; no software is downloaded automatically.")
    if digest(archive.read_bytes()) != ARCHIVE_HASH:
        raise RuntimeError("The Pandoc archive failed its integrity check.")
    # Extract one fixed member into a fixed private file, never archive paths.
    with tarfile.open(archive, "r:gz") as pack:
        member = pack.getmember("pandoc-3.6.4/bin/pandoc")
        if not member.isfile():
            raise RuntimeError("Unexpected Pandoc archive member")
        with pack.extractfile(member) as source, (work / "pandoc").open("wb") as target:
            shutil.copyfileobj(source, target)
    (work / "pandoc").chmod(0o700)


def validate_pdf(work):
    pdf = work / "book.pdf"
    run(["qpdf", "--check", str(pdf)], work, "qpdf-check.txt")
    run(["pdftotext", "-bbox-layout", str(pdf), str(work / "bbox.html")], work, "text-check.txt")
    pages = ET.parse(work / "bbox.html").findall(".//{http://www.w3.org/1999/xhtml}page")
    outside = []
    for number, page in enumerate(pages, 1):
        width, height = float(page.attrib["width"]), float(page.attrib["height"])
        for word in page.findall(".//{http://www.w3.org/1999/xhtml}word"):
            x0, y0, x1, y1 = (float(word.attrib[k]) for k in ("xMin", "yMin", "xMax", "yMax"))
            if min(x0, y0) < -0.1 or x1 > width + 0.1 or y1 > height + 0.1:
                outside.append({"page": number, "text": word.text})
    log = (work / "book.log").read_text(errors="replace")
    warnings = {key: re.findall(pattern, log) for key, pattern in {
        "missing_glyphs": r"Missing character[^\n]*",
        "horizontal_overflow": r"Overfull \\hbox[^\n]*",
        "vertical_overflow": r"Overfull \\vbox[^\n]*",
        "unresolved_references": r"LaTeX Warning:[^\n]*(?:undefined|Label\(s\) may have changed)[^\n]*",
    }.items()}
    scaled = []
    for eid, width, available in re.findall(r"EXPORT-SCALED (E\d+): width=([\d.]+)pt; available=([\d.]+)pt", log):
        scaled.append({"id": eid, "scale": float(available) / float(width)})
    result = {"pages": len(pages), "outside_page": outside, "warnings": warnings, "resized_equations": scaled}
    (work / "render-checks.json").write_text(json.dumps(result, indent=2) + "\n")
    if not pages or outside or any(warnings.values()):
        raise RuntimeError(f"The export failed a rendering check. Details: {work / 'render-checks.json'}")
    if any(x["scale"] < 0.6 for x in scaled):
        raise RuntimeError("An equation would be reduced below 60% size; a PDF-only layout adjustment is needed. See equation-index.json and render-checks.json in the build folder.")
    return result


def atomic_copy(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".pde-pdf-", dir=destination.parent)
    try:
        with os.fdopen(fd, "wb") as target, source.open("rb") as origin:
            shutil.copyfileobj(origin, target)
            target.flush()
            os.fsync(target.fileno())
        os.replace(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build the current PDE book PDF without changing the repository.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("output", nargs="?", type=Path, default=DEFAULT_OUTPUT, help="PDF destination, outside the repository")
    parser.add_argument("--repo", type=Path, default=DEFAULT_REPO, help="Repository to read")
    parser.add_argument("--pandoc-archive", type=Path, help="Verified Pandoc 3.6.4 Linux x86-64 release archive; overrides installed Pandoc and the user cache")
    parser.add_argument("--keep-build", action="store_true", help="Keep the temporary snapshot, generated TeX and logs after success")
    args = parser.parse_args(argv)
    repo = args.repo.expanduser().resolve()
    output = args.output.expanduser().absolute()
    # Resolving the parent also catches paths through symlinked source folders.
    output = output.parent.resolve() / output.name
    if output.is_symlink():
        parser.error("Refusing to replace a symlink; choose a regular PDF destination")
    try:
        validate_output(repo, output)
        for command in ("xelatex", "qpdf", "pdftotext"):
            if not shutil.which(command):
                raise RuntimeError(f"Required command not found: {command}. No software is installed automatically.")
    except (ValueError, RuntimeError) as error:
        parser.error(str(error))
    # Do not honor a TMPDIR pointing into the live repository.
    build_parent = Path("/tmp").resolve()
    if build_parent.is_relative_to(repo):
        parser.error("The source repository must not contain the temporary-build directory /tmp")
    work = Path(tempfile.mkdtemp(prefix="pde-pdf-", dir=build_parent))
    succeeded = False
    try:
        print(f"Reading book: {repo}", flush=True)
        files, unlisted, payload = snapshot(repo, work)
        if unlisted:
            print("Additional Markdown included after guide-listed chapters: " + ", ".join(unlisted), flush=True)
        moment = datetime.now().astimezone()
        date = f"{moment.day} {moment.strftime('%B %Y')}"
        config = {"files": files, "date": date}
        (work / "build-config.json").write_text(json.dumps(config, indent=2) + "\n")
        shutil.copyfile(BUNDLE / "layout.tex", work / "layout.tex")
        install_private_converter(work, args.pandoc_archive)
        print(f"Typesetting {len(files)} source documents in a private snapshot…", flush=True)
        run([sys.executable, "-B", str(BUNDLE / "render_book.py"), str(work)], work, "conversion.txt")
        for number in range(1, 6):
            print(f"  PDF pass {number}", flush=True)
            run(["xelatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "book.tex"], work, f"xelatex-pass-{number}.txt")
            log = (work / "book.log").read_text(errors="replace")
            unsettled = re.search(r"Rerun to|Label\(s\) may have changed|There were undefined references", log)
            if number >= 2 and not unsettled:
                break
        else:
            raise RuntimeError("Cross-references did not stabilize after five passes")
        checks = validate_pdf(work)
        changed = []
        for name, data in payload.items():
            if not (repo / name).is_file() or (repo / name).read_bytes() != data:
                changed.append(name)
        current_files = discover(repo)[0]
        changed_inventory = current_files != files
        receipt = {
            "created_at": moment.isoformat(), "repository": str(repo), "pdf": str(output),
            "pdf_sha256": digest((work / "book.pdf").read_bytes()),
            "source_manifest": json.loads((work / "source-manifest.json").read_text()),
            "coverage": json.loads((work / "coverage.json").read_text()), "render_checks": checks,
            "concurrent_source_changes": changed, "concurrent_inventory_change": changed_inventory,
            "scope": "PDF rendering checks only, not mathematical proof validation; no repository writes.",
        }
        (work / "build-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
        # A failed conversion/check never touches an earlier successful PDF.
        atomic_copy(work / "book.pdf", output)
        atomic_copy(work / "build-receipt.json", output.with_suffix(".build.json"))
        succeeded = True
        print(f"PDF ready: {output}\nPages: {checks['pages']}\nChecks: {output.with_suffix('.build.json')}", flush=True)
        if changed or changed_inventory:
            print("Note: the repository changed during typesetting. This PDF contains the captured snapshot; rerun for newer edits.", flush=True)
        if args.keep_build:
            print(f"Build files: {work}", flush=True)
        return 0
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f"PDF export stopped: {error}\nDiagnostics retained: {work}\nThe exporter made no repository writes.", file=sys.stderr)
        return 1
    finally:
        if succeeded and not args.keep_build:
            # Only this process's newly created private temporary directory.
            shutil.rmtree(work)


if __name__ == "__main__":
    raise SystemExit(main())
