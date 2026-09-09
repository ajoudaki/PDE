"""Private acceptance instrumentation; never imported by repository code on disk."""
import importlib.util
import json
import os
from pathlib import Path
import sys
import types

BASE = Path('/tmp/resnet-patch-acceptance.7tppNkr4')
REPO = Path('/home/amir/Codes/PDE')
LONG = REPO / 'studies/resnet_dense_long_horizon'
WRAPPER = LONG / 'reproduce.sh'
MANIFEST = LONG / 'make_manifest.py'
LINKS = REPO / 'studies/_output_paths.py'
TEST = REPO / 'studies/repository_refactor_2026_09_09/test_resnet_routing.py'
ALLOWED = {str(p) for p in (WRAPPER, MANIFEST, LINKS, TEST)}
QUERY = ('import sys; from pathlib import Path; from make_manifest import '
         'validate_output_root; print(validate_output_root(Path(sys.argv[1])))')


def event(kind, **fields):
    target = os.environ.get('PATCH_EVENT_LOG')
    if target:
        with open(target, 'a', encoding='utf-8') as stream:
            stream.write(json.dumps({'kind': kind, **fields}, ensure_ascii=True) + '\n')


def install_audit():
    def absolute(path):
        if isinstance(path, int) or path is None:
            return None
        return os.path.abspath(os.fsdecode(path))

    def private_write(path):
        normalized = absolute(path)
        if normalized is not None and not (normalized == str(BASE) or normalized.startswith(str(BASE) + '/')):
            raise PermissionError('acceptance harness forbids write outside private directory: ' + normalized)

    def audit(name, args):
        if name == 'open':
            path, mode, flags = args
            normalized = absolute(path)
            if normalized and (normalized == str(REPO) or normalized.startswith(str(REPO) + '/')):
                if normalized not in ALLOWED:
                    raise PermissionError('acceptance harness forbids reading unapproved repository file: ' + normalized)
            if flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
                private_write(path)
        elif name in {'os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.truncate', 'os.utime'}:
            private_write(args[0])
        elif name in {'os.rename', 'os.link'}:
            private_write(args[0])
            private_write(args[1])
        elif name == 'os.symlink':
            private_write(args[1])
        elif name in {'socket.connect', 'socket.bind'}:
            raise PermissionError('acceptance harness forbids network access')
    sys.addaudithook(audit)


def load_real_guards():
    # Supply only a namespace shell, so no unapproved studies/__init__.py is read.
    package = types.ModuleType('studies')
    package.__path__ = []
    sys.modules['studies'] = package
    for name, path in (('studies._output_paths', LINKS), ('make_manifest', MANIFEST)):
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    package._output_paths = sys.modules['studies._output_paths']

    def profile(frame, kind, arg):
        if kind == 'call':
            code = frame.f_code
            if code.co_filename == str(MANIFEST) and code.co_name == 'validate_output_root':
                event('validate_call', selected=str(frame.f_locals['path']))
            elif code.co_filename == str(LINKS) and code.co_name == 'reject_output_links':
                event('link_guard_call', selected=str(frame.f_locals['path']))
    sys.setprofile(profile)

