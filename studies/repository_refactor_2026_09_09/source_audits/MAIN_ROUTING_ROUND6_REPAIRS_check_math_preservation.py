"""Compare full function/class ASTs after removing only enumerated routing edits."""
import ast
import copy
import hashlib
import json
from pathlib import Path

REPO = Path('/home/amir/Codes/PDE')
BASE = Path('/tmp/pde-f3-f4-worker-hwv1KBBr')
before = json.loads((BASE / 'ast.before.json').read_text())

def text(node):
    return ast.unparse(node)

class RemoveRouting(ast.NodeTransformer):
    def __init__(self, path, name):
        self.path, self.name = path, name
        self.removed = []

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'reject_output_links':
            self.removed.append(text(node))
            return None
        return self.generic_visit(node)

    def visit_Assign(self, node):
        target = text(node.targets[0]) if len(node.targets) == 1 else ''
        value = text(node.value)
        if target in ('out_dir', 'path', 'args.output') and value == target + '.expanduser().absolute()':
            self.removed.append(text(node))
            return None
        if self.name == 'main' and 'resnet_dense_early_audit/' in self.path and target in ('out_dir', 'out'):
            if value == target + '.resolve()':
                self.removed.append(text(node))
                return None
            if value.startswith('Path(') and value.endswith('.expanduser().absolute()'):
                self.removed.append(text(node))
                node.value = ast.parse(value.removesuffix('.expanduser().absolute()') + '.resolve()', mode='eval').body
                return node
        if self.path.endswith('/runtime_paths.py') and self.name == 'output_root':
            if target == 'selected' and value.endswith('.expanduser().absolute()'):
                self.removed.append(text(node))
                node.targets = [ast.Name(id='path', ctx=ast.Store())]
                node.value = ast.parse(value.removesuffix('.absolute()') + '.resolve()', mode='eval').body
                return node
            if target == 'path' and value == 'selected.resolve()':
                self.removed.append(text(node))
                return None
        return self.generic_visit(node)

checked = 0
routed = []
failures = []
for relative, expected in before.items():
    tree = ast.parse((REPO / relative).read_text())
    nodes = {node.name: node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef))}
    if set(nodes) != set(expected):
        failures.append({'file': relative, 'failure': 'function/class inventory changed'})
    for name, node in nodes.items():
        transform = RemoveRouting(relative, name)
        normalized = transform.visit(copy.deepcopy(node))
        digest = hashlib.sha256(ast.dump(normalized, include_attributes=False).encode()).hexdigest()
        checked += 1
        if digest != expected.get(name):
            failures.append({'file': relative, 'function': name, 'failure': 'non-routing AST changed'})
        if transform.removed:
            routed.append({'file': relative, 'function': name, 'routing_edits': transform.removed,
                           'preserved_body_sha256': digest})
print(json.dumps({'files': len(before), 'functions_and_classes': checked,
                  'normalized_routing_boundaries': routed, 'failures': failures}, indent=2))
assert not failures, failures
