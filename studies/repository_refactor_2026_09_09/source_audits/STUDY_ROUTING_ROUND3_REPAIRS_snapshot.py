"""Private before/after byte and AST evidence; never writes into the repository."""
import ast
import difflib
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path("/home/amir/Codes/PDE")
PRIVATE = Path(__file__).parent
NAMES = ("resnet_generalization", "resnet_proof_audit", "resnet_activation_controls",
         "stieltjes_finite_width", "stieltjes_direct_loewner",
         "stieltjes_hybrid_campaign", "stieltjes_proxy_campaign")

def inventory():
    command = ["rg", "--files", "--hidden", *["studies/" + name for name in NAMES],
               "-g", "*.py", "-g", "*.sh", "-g", "*.json", "-g", "README.md",
               "-g", "REPRODUCTION.md", "-g", "*SHA256*", "-g", "!**/audits/**",
               "-g", "!stage0_contact_audit.json"]
    return sorted(subprocess.check_output(command, cwd=ROOT, text=True).splitlines()) + ["studies/_output_paths.py"]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def functions(data):
    tree = ast.parse(data)
    result = {}
    def visit(nodes, prefix=""):
        for node in nodes:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                key = prefix + node.name
                result[key] = digest(ast.dump(node, include_attributes=False).encode())
                visit(node.body, key + ".")
    visit(tree.body)
    return result

stage = sys.argv[1]
assert stage in ("before", "after")
paths = inventory()
records = {}
for relative in paths:
    payload = (ROOT / relative).read_bytes()
    records[relative] = digest(payload)
    if stage == "before":
        copy = PRIVATE / "before" / relative
        copy.parent.mkdir(parents=True, exist_ok=True)
        copy.write_bytes(payload)
(PRIVATE / (stage + ".sha256")).write_text(
    "".join(value + "  " + name + "\n" for name, value in records.items()))
(PRIVATE / (stage + ".json")).write_text(json.dumps(records, indent=2) + "\n")
if stage == "after":
    old = json.loads((PRIVATE / "before.json").read_text())
    changed = [name for name in records if old.get(name) != records[name]]
    deleted = sorted(old.keys() - records.keys())
    diff = []
    ast_records = {}
    for name in changed:
        previous = (PRIVATE / "before" / name)
        before = previous.read_text() if previous.exists() else ""
        after = (ROOT / name).read_text()
        diff.extend(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                        fromfile="a/" + name if previous.exists() else "/dev/null",
                                        tofile="b/" + name))
        if name.endswith(".py"):
            a, b = functions(before), functions(after)
            ast_records[name] = {"before": a, "after": b,
                "changed_functions": sorted(k for k in a.keys() & b.keys() if a[k] != b[k]),
                "unchanged_functions": sorted(k for k in a.keys() & b.keys() if a[k] == b[k]),
                "added_functions": sorted(b.keys() - a.keys()),
                "deleted_functions": sorted(a.keys() - b.keys())}
    (PRIVATE / "changes.patch").write_text("".join(diff))
    (PRIVATE / "function-ast.json").write_text(json.dumps(ast_records, indent=2) + "\n")
    (PRIVATE / "changed-files.json").write_text(json.dumps({"changed": changed, "deleted": deleted}, indent=2) + "\n")
    assert not deleted
    assert records["studies/_output_paths.py"] == old["studies/_output_paths.py"] == "8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e"
    print(json.dumps({"changed": changed, "unchanged_count": len(records) - len(changed)}, indent=2))
print(stage, len(records), "files")
