"""Private read-hash instrumentation and repository-write refusal for this review."""
import hashlib
import json
import os
from pathlib import Path
import sys

REPO = Path('/home/amir/Codes/PDE')
PRIVATE = Path('/tmp/pde-patch-acceptance.iUBcgMxi')
seen = set()
busy = False

def snapshot(value):
    global busy
    if busy or not isinstance(value, (str, bytes, os.PathLike)):
        return
    path = Path(os.fsdecode(value)).absolute()
    if not path.is_relative_to(REPO) or path in seen or not path.is_file():
        return
    busy = True
    try:
        data = path.read_bytes()
        row = {'path': str(path), 'sha256': hashlib.sha256(data).hexdigest(),
               'size': len(data), 'pid': os.getpid()}
        with (PRIVATE / 'read_hashes.jsonl').open('a') as stream:
            stream.write(json.dumps(row) + '\n')
        seen.add(path)
    finally:
        busy = False

def audit(event, args):
    if busy:
        return
    if event == 'open':
        name, mode, flags = args
        if isinstance(name, (str, bytes, os.PathLike)):
            path = Path(os.fsdecode(name)).absolute()
            writing = flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
            if writing and path.is_relative_to(REPO):
                raise RuntimeError('Review refused repository write: ' + str(path))
            if not writing:
                snapshot(path)
    if event in {'os.mkdir', 'os.remove', 'os.rmdir', 'os.rename', 'os.link', 'os.symlink'}:
        if event == 'os.rename':
            targets = ((args[0], args[2]), (args[1], args[3]))
        elif event == 'os.link':
            targets = ((args[1], args[3]),)
        elif event == 'os.symlink':
            targets = ((args[1], args[2]),)
        elif event == 'os.mkdir':
            targets = ((args[0], args[2]),)
        else:
            targets = ((args[0], args[1]),)
        for name, dir_fd in targets:
            if isinstance(name, (str, bytes, os.PathLike)):
                path = Path(os.fsdecode(name))
                if not path.is_absolute() and dir_fd not in (-1, None):
                    path = Path(os.readlink('/proc/self/fd/' + str(dir_fd))) / path
                path = path.absolute()
                if path.is_relative_to(REPO):
                    raise RuntimeError('Review refused repository mutation: ' + str(path))

sys.dont_write_bytecode = True
sys.addaudithook(audit)
