"""Compare whole function ASTs after only enumerated boundary normalizations."""
import ast
import copy
import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path("/home/amir/Codes/PDE")
PRIVATE = Path(__file__).parent
records = json.loads((PRIVATE / "function-ast.json").read_text())
before_hashes = json.loads((PRIVATE / "before.json").read_text())
after_hashes = json.loads((PRIVATE / "after.json").read_text())
results = []

def dump(node):
    return ast.dump(node, include_attributes=False)

def sha(value):
    return hashlib.sha256(value.encode()).hexdigest()

def binding(node):
    if isinstance(node, ast.Assign):
        return {ast.unparse(t) for t in node.targets}
    return set()

def method(node):
    return ast.unparse(node.func) if isinstance(node, ast.Call) else ""

GUARDS = {"require_output", "PATHS.require_output", "require_raw_output",
          "require_analysis_output", "require_current_authorization"}

def guard(node):
    if isinstance(node, (ast.Assign, ast.Expr)):
        return method(node.value) in GUARDS
    return False

class BoundaryOnly(ast.NodeTransformer):
    def __init__(self, relative, function):
        self.relative, self.function = relative, function
        self.raw = relative.endswith(("/run_pde.py", "/run_exact_reference.py"))

    def visit_Expr(self, node):
        return None if guard(node) else self.generic_visit(node)

    def visit_Assign(self, node):
        names = binding(node)
        if guard(node):
            return None
        if self.raw and names & {"scientific_config", "scientific_config_sha256", "output_dir",
                                 "path", "partial", "case_tag", "hash_tag", "name"}:
            return None
        if self.function == "run_analysis" and names == {"output_dir"}:
            return None
        if self.function == "discover_evidence" and names == {"processed_root"}:
            return None
        if self.relative.endswith("/width_analysis.py") and names == {"input_paths"}:
            return None
        if self.relative.endswith("/gd_vs_rk4_n4096.py") and names == {"ref"}:
            return None
        if self.relative.endswith("/gd_vs_rk4_n8192_point.py") and names & {"reference", "suffix", "output_path"}:
            return None
        if self.function == "_require_seal_common" and names == {"path"}:
            old = ast.parse("path = ROOT / relative").body[0]
            new = ast.parse("path = RESULTS.parent / relative").body[0]
            assert dump(node) in (dump(old), dump(new))
            return new
        return self.generic_visit(node)

    def visit_If(self, node):
        if not node.orelse and node.body and all(guard(n) for n in node.body):
            return None
        text = ast.unparse(node.test)
        if self.raw and (text == "args.integrator != 'rk4'" or text == "start_time"):
            assert all(isinstance(n, ast.Assign) and binding(n) == {"name"} for n in node.body)
            return None
        if self.raw and "path == Path(args.restart_from).resolve()" in text:
            return None
        if self.function == "run_analysis" and text.startswith("output_dir.is_relative_to("):
            return None
        if self.function == "write_processed" and text.startswith("context.processed_root.resolve().is_relative_to("):
            return None
        if self.function == "load_reference_run" and text == "config_path is None":
            return None
        if self.relative.endswith("/gd_vs_rk4_n8192_point.py") and text == "not REFERENCE_NPZ.is_file()":
            assert ast.unparse(node.body[0]) == "raise FileNotFoundError(REFERENCE_NPZ)"
            return None
        if self.relative.endswith("/gd_vs_rk4_n4096.py") and text == "not REFERENCE_NPZ.exists()":
            node.test = ast.parse("not REFERENCE_NPZ.is_file()", mode="eval").body
        return self.generic_visit(node)

    def visit_Call(self, node):
        if method(node) == "partial.open":
            assert len(node.args) == 1 and isinstance(node.args[0], ast.Constant)
            assert node.args[0].value in ("w", "wb", "x", "xb")
            node.args[0] = ast.Constant("exclusive-binary" if "b" in node.args[0].value else "exclusive-text")
        return self.generic_visit(node)

    def visit_Name(self, node):
        if self.relative.endswith(("/run_fresh_order13_median.py", "/run_fresh_calibrated_ratio.py")) and node.id == "PEELING":
            node.id = "MFP_COMPILER"
        return node

def assignment(function, name):
    nodes = [n for n in function.body if binding(n) == {name}]
    assert len(nodes) == 1, (function.name, name, len(nodes))
    return nodes[0]

for relative, record in records.items():
    if "/tests/" in relative or Path(relative).name.startswith("test_"):
        continue
    old_path, new_path = PRIVATE / "before" / relative, ROOT / relative
    if not old_path.exists():
        results.append(dict(file=relative, new_boundary_module=True))
        continue
    old_tree, new_tree = ast.parse(old_path.read_text()), ast.parse(new_path.read_text())
    old_functions = {n.name: n for n in old_tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    new_functions = {n.name: n for n in new_tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    assert not record["deleted_functions"], relative
    # All original module-level assignments (including caps, seeds and paths)
    # remain exactly the same. PATHS is the only newly introduced assignment.
    old_constants = {tuple(sorted(binding(n))): dump(n) for n in old_tree.body if isinstance(n, ast.Assign)}
    new_constants = {tuple(sorted(binding(n))): dump(n) for n in new_tree.body if isinstance(n, ast.Assign)}
    assert all(new_constants.get(k) == v for k, v in old_constants.items()), relative
    checked = []
    for name in record["changed_functions"]:
        a, b = old_functions[name], new_functions[name]
        moved = []
        if relative.endswith(("/run_pde.py", "/run_exact_reference.py")):
            moved = ["scientific_config", "scientific_config_sha256"]
        elif relative.endswith("/gd_vs_rk4_n4096.py"):
            moved = ["ref"]
        elif relative.endswith("/gd_vs_rk4_n8192_point.py"):
            moved = ["reference", "suffix", "output_path"]
        moved_hashes = {}
        for variable in moved:
            old_node, new_node = assignment(a, variable), assignment(b, variable)
            assert dump(old_node) == dump(new_node), (relative, variable)
            moved_hashes[variable] = sha(dump(old_node))
        normal_a = BoundaryOnly(relative, name).visit(copy.deepcopy(a))
        normal_b = BoundaryOnly(relative, name).visit(copy.deepcopy(b))
        if dump(normal_a) != dump(normal_b):
            difference = list(difflib.unified_diff(ast.unparse(ast.fix_missing_locations(normal_a)).splitlines(),
                              ast.unparse(ast.fix_missing_locations(normal_b)).splitlines(), n=2))
            raise AssertionError((relative, name, "\n".join(difference[:60])))
        checked.append(dict(function=name, normalized_before_sha256=sha(dump(normal_a)),
                            normalized_after_sha256=sha(dump(normal_b)), exact_moved_assignments=moved_hashes))
    results.append(dict(file=relative, unchanged_functions=record["unchanged_functions"],
                        changed_boundary_functions=checked, added_boundary_functions=record["added_functions"],
                        existing_module_assignments_preserved=True))

unchanged_contracts = [p for p in before_hashes if p.endswith((".json", ".sh")) or "SHA256" in Path(p).name]
assert all(before_hashes[p] == after_hashes[p] for p in unchanged_contracts)
assert before_hashes["studies/_output_paths.py"] == after_hashes["studies/_output_paths.py"] == "8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e"
payload = dict(status="PASS", normalization_scope="enumerated path/guard/partial-open changes only; exact moved assignment AST checks",
               unchanged_configuration_hash_shell_files=unchanged_contracts, functions=results)
(PRIVATE / "preservation.json").write_text(json.dumps(payload, indent=2) + "\n")
print(json.dumps(dict(status="PASS", implementation_files=len(results),
                     unchanged_functions=sum(len(r.get("unchanged_functions", [])) for r in results),
                     normalized_boundary_functions=sum(len(r.get("changed_boundary_functions", [])) for r in results),
                     unchanged_contract_files=len(unchanged_contracts))))
