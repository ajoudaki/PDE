"""Freeze only import dependencies and exact regression/selection references."""
import ast
import hashlib
import json
from pathlib import Path
import shutil

BASE = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).parent
DEST = PRIVATE / 'snapshot'
EXCLUDED = {'test_selected_sine_fixture_to_separate_fresh_result',
            'test_freeze_refuses_existing_seal_without_any_writes',
            'test_compiler_package_dispatches_retained_gate_before_science'}
seen = set()
pending = list(DEST.rglob('*.py'))
g = 'studies/mfp_gaussian_calculus/'
extra = [
 'order5/compiler/generate_artifacts.py', 'order5/compiler/build_self_contained_report.py',
 'order5/independent/freeze_tagged.py', 'order5/independent/interpolate_symbolic_q0.py',
 'order5/independent/independent_compiler.py', 'depth_order5/primary/generate_frozen_artifacts.py',
 'depth_order5/primary/build_self_contained_report.py', 'depth_order5/primary/compare_frozen_routes.py',
 'depth_order5_scalar/independent/forward_contraction.py',
 'depth_order5_scalar/independent/reverse_contraction.py',
 'depth_order5_scalar/independent/moving_contraction.py',
 'depth_order5_scalar/multi_observable/independent_route_a/gamma04_contraction.py',
 'depth_order5_observables/independent/gamma04_contraction.py',
 'depth_order5_scalar/independent/build_full_report.py',
 'depth_order5_observables/independent/reduce_frozen_head.py',
 'order5/run_checks.py', 'order5/audit_hostile.py',
 'depth_order5_scalar/independent/depth_assembler.py',
]
copied = []

def add(rel):
    src, dst = BASE / rel, DEST / rel
    if not src.is_file():
        return
    if not dst.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied.append(str(rel))
    if dst.suffix == '.py' and dst not in seen:
        pending.append(dst)

def add_module(name, local):
    rel = Path(*name.split('.'))
    for candidate in (rel.with_suffix('.py'), rel / '__init__.py'):
        if (BASE / candidate).is_file():
            add(candidate)
            for parent in candidate.parents:
                if str(parent) != '.':
                    add(parent / '__init__.py')
            return
    # Script-oriented sibling and parent imports only.
    if '.' not in name:
        for directory in (local.parent, local.parent.parent):
            candidate = directory / (name + '.py')
            if (BASE / candidate).is_file():
                add(candidate)
                return

for rel in extra:
    add(g + rel)
for rel in (
    g + 'depth_order5/primary/PRIMARY_FREEZE_MANIFEST.json',
    g + 'depth_order5/primary/PRIMARY_FREEZE_SHA256.txt',
    g + 'depth_order5/independent/FROZEN_MANIFEST.json',
    g + 'depth_order5/independent/FROZEN_MANIFEST_SHA256.txt',
):
    add(rel)

class Imports(ast.NodeVisitor):
    def __init__(self, rel):
        self.rel = rel
        self.package = list(rel.parent.parts)
    def visit_FunctionDef(self, node):
        if node.name not in EXCLUDED:
            self.generic_visit(node)
    def visit_Import(self, node):
        for alias in node.names:
            add_module(alias.name, self.rel)
    def visit_ImportFrom(self, node):
        prefix = self.package[:len(self.package) - node.level + 1] if node.level else []
        if node.module:
            prefix += node.module.split('.')
        base = '.'.join(prefix)
        if base:
            add_module(base, self.rel)
        for alias in node.names:
            add_module('.'.join(prefix + [alias.name]), self.rel)

while pending:
    path = pending.pop()
    if path in seen:
        continue
    seen.add(path)
    rel = path.relative_to(DEST)
    for parent in rel.parents:
        if str(parent) != '.':
            add(parent / '__init__.py')
    Imports(rel).visit(ast.parse(path.read_text(), filename=str(rel)))

inventory = []
for path in sorted(p for p in DEST.rglob('*') if p.is_file()):
    rel = path.relative_to(DEST)
    raw = path.read_bytes()
    inventory.append({'path': str(rel), 'before_sha256': hashlib.sha256(raw).hexdigest(),
                      'bytes': len(raw), 'lines': len(raw.splitlines())})
(PRIVATE / 'frozen_inventory.json').write_text(json.dumps(inventory, indent=2) + '\n')
print(json.dumps({'new_dependencies': copied, 'frozen_files': len(inventory)}, indent=2))
