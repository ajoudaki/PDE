"""Fresh static integration probes; no trajectories or empirical accuracy runs."""
from pathlib import Path
from fractions import Fraction
import difflib
import hashlib
import json
import os
import re
import sys
import numpy as np

ROOT = Path('/home/amir/Codes/PDE')
OUT = ROOT / 'data/generated/observable_hierarchy/H2_integration_v3'
EDITION = OUT / 'edition'
STUDY = ROOT / 'studies/observable_hierarchy'
sys.path.insert(0, str(EDITION / 'code'))
from pde import observable_closure as core

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = json.loads((STUDY / 'H2_integration_inputs_v3.json').read_text())
inputs = {}
for relative, record in manifest['inputs'].items():
    actual = digest(ROOT / relative)
    assert actual == record['sha256'], relative
    inputs[relative] = dict(sha256=actual, lines=len((ROOT / relative).read_bytes().splitlines()))
inputs['studies/observable_hierarchy/H2_integration_inputs_v3.json'] = dict(
    sha256=digest(STUDY / 'H2_integration_inputs_v3.json'))

guides = (STUDY / 'H2_guides_v1.md').read_text()
guide_sources = []
for part in guides.split('\n---\n'):
    if part.lstrip().startswith('Source:'):
        header, body = part.strip().split('\n\n', 1)
        relative = header.split('`')[1]
        assert body.rstrip() == (ROOT / relative).read_text().rstrip(), relative
        guide_sources.append(relative)

proposal = (STUDY / 'H2_proposed_section_v3.md').read_bytes().rstrip() + b'\n\n'
old = (ROOT / 'docs/global_nonlinear.md').read_bytes()
new = (EDITION / 'docs/global_nonlinear.md').read_bytes()
anchor = b'#### C.4.8. Sampling fluctuations of the trained prediction'
assert old.count(anchor) == new.count(anchor) == 1
assert new == old.replace(anchor, proposal + anchor)
assert new.replace(proposal, b'', 1) == old
candidate = (STUDY / 'candidate_v3.md').read_bytes().rstrip()
assert old.count(candidate) == new.count(candidate) == 1
assert old.index(candidate) == new.index(candidate)

assembly = json.loads((EDITION / 'ASSEMBLY.json').read_text())
preserved = []
for relative in assembly['inputs']['copy_sources']:
    if relative not in ('docs/global_nonlinear.md', 'docs/README.md', 'code/README.md'):
        assert (ROOT / relative).read_bytes() == (EDITION / relative).read_bytes(), relative
        preserved.append(relative)
for target, source in [('docs/README.md','H2_docs_README_v3.md'),
                       ('code/README.md','H2_code_README_v3.md'),
                       ('code/pde/observable_closure.py','H2_prototype_v3.py')]:
    assert (EDITION / target).read_bytes() == (STUDY / source).read_bytes()
source_test = (STUDY / 'H2_test_prototype_v3.py').read_text()
expected_test = source_test.replace(
    'os.environ.get("H2_PROTOTYPE_MODULE", "H2_prototype_v3")',
    'os.environ.get("H2_PROTOTYPE_MODULE", "pde.observable_closure")').replace(
    'Set H2_PROTOTYPE_MODULE=pde.observable_closure after a reviewed relocation.\n'
    'The default imports the study-owned prototype beside this file.',
    'The default imports pde.observable_closure from the installed package.\n'
    'H2_PROTOTYPE_MODULE may override that import for isolated checks.')
assert (EDITION / 'code/tests/test_observable_closure.py').read_text() == expected_test
assert (EDITION / 'code/README.md').read_bytes().startswith((ROOT / 'code/README.md').read_bytes())
assert not (EDITION / 'studies').exists()
assert not (EDITION / '.git').exists()
assert not (EDITION / 'data').exists()
assert Path(core.__file__).resolve() == EDITION / 'code/pde/observable_closure.py'

changes = {}
new_links = []
for relative in ('docs/README.md','code/README.md'):
    a = (ROOT / relative).read_text().splitlines(True)
    b = (EDITION / relative).read_text().splitlines(True)
    operations = difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes()
    changes[relative] = operations
    for tag, i, j, k, l in operations:
        if tag != 'equal':
            for target in re.findall(r'\]\(([^)]+)\)', ''.join(b[k:l])):
                file_part, _, fragment = target.partition('#')
                path = (EDITION / relative).parent / file_part
                assert path.is_file(), target
                if fragment:
                    headings = re.findall(r'^#+\s+(.+)$',path.read_text(),flags=re.M)
                    slugs = {re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in headings}
                    assert fragment in slugs, target
                new_links.append(target)

# Unequal populations, nonuniform probabilities, multiple arbitrary current
# coordinates for the same frozen marks. This state has no initializer metadata.
state = core.State(
    core.Population1([[1., .2], [1., -.4], [1., .2]],
                     [[0., .3], [.4, -.2], [0., .3]],
                     [[.2, .1], [.3, -.4], [-.5, .7]], [.2,.3,.5]),
    core.Population2([[1., .1], [1., -.3]], [.4,-.2], [.7,.3]),
    [[.3,-.1],[.2,.4]], [[.2,.05],[-.1,.3]])
data = core.DataLaw([[1.,0.],[.6,.8]], [.8,-.4], [.35,.65])
f = core.fields(state,data.inputs)
velocity = core.rhs(state,data)
epsilon = 1e-6
errors = {}
for name, array in [('w',state.first.w),('c',state.second.c),('M',state.M)]:
    local=[]
    for index in np.ndindex(array.shape):
        plus,minus=state.copy(),state.copy()
        ap = plus.first.w if name=='w' else plus.second.c if name=='c' else plus.M
        am = minus.first.w if name=='w' else minus.second.c if name=='c' else minus.M
        ap[index]+=epsilon; am[index]-=epsilon
        fd=(core.loss(plus,data)-core.loss(minus,data))/(2*epsilon)
        weight = state.first.probabilities[index[0]] if name=='w' else state.second.probabilities[index[0]] if name=='c' else 1
        local.append(abs(fd + weight*getattr(velocity,name)[index]))
    errors[name]=max(local)
    assert errors[name] < 2e-10

# Saved-state completeness includes distinct conditional current values, D and
# all optional ordinary JSON provenance, and requires no source compiler.
word=core.action(core.unary('sin',core.action(core.unary('tanh',core.seed('w1')))))
frozen=core.frozen_z20((.6,.8))
frozen_before=core.observe(state,frozen)
updated=core.algebraic_update(state,velocity,.001)
assert np.array_equal(core.observe(updated,frozen),frozen_before)
metadata_cases=[{}, {'note':'supplied','nested':{'a':[1,True,None]}}, {'format':'caller-stale','note':'writer owns schema'}]
for i,metadata in enumerate(metadata_cases):
    updated.metadata=metadata.copy()
    archive=OUT / f'independent_restart_{i}.npz'
    core.save_restart(archive,updated,data)
    assert updated.metadata == metadata
    restored, restored_data=core.load_restart(archive)
    assert restored.metadata == dict(metadata,format='C-H2-quadrature-v1')
    for pop in ('first','second'):
        for key in vars(getattr(updated,pop)):
            assert np.array_equal(getattr(getattr(updated,pop),key),getattr(getattr(restored,pop),key))
    for key in ('M','D'):
        assert np.array_equal(getattr(updated,key),getattr(restored,key))
    for key in ('w','c','M'):
        assert np.array_equal(getattr(core.rhs(restored,restored_data),key),getattr(core.rhs(updated,data),key))
    assert np.array_equal(core.observe(restored,word),core.observe(updated,word))
    assert np.array_equal(core.observe(restored,frozen),core.observe(updated,frozen))

# Reordering each carrier leaves law-level prediction and M velocity invariant,
# while every individual coordinate velocity follows that same permutation.
pi1,pi2=np.array([2,0,1]),np.array([1,0])
permuted=core.State(
    core.Population1(state.first.b[pi1],state.first.g[pi1],state.first.w[pi1],state.first.probabilities[pi1]),
    core.Population2(state.second.b[pi2],state.second.c[pi2],state.second.probabilities[pi2]),state.M,state.D)
np.testing.assert_allclose(core.fields(permuted,data.inputs)['f'],f['f'],rtol=0,atol=2e-16)
vp=core.rhs(permuted,data)
np.testing.assert_allclose(vp.M,velocity.M,rtol=0,atol=2e-16)
np.testing.assert_allclose(vp.w,velocity.w[pi1],rtol=0,atol=2e-16)
np.testing.assert_allclose(vp.c,velocity.c[pi2],rtol=0,atol=2e-16)

# Rational graph and current/frozen observation semantics on explicit arrays.
rational=core.scale(Fraction(2,3),core.unary('sin',core.seed('w1')))
np.testing.assert_array_equal(core.observe(state,rational),(2/3)*np.sin(state.first.w[:,0]))
joint,p=core.joint_observe(state,[core.seed('g1'),core.seed('w1'),word])
assert np.array_equal(joint[:,0],state.first.g[:,0])
assert np.array_equal(joint[:,1],state.first.w[:,0])
assert np.array_equal(p,state.first.probabilities)
joint[:]=123
assert not np.any(state.first.w==123)

# Initialization is deterministic, retains both orientations and no RNG input;
# this check records the producer, without testing quadrature convergence.
s0,program=core.initialize(1)
s1,program1=core.initialize(1)
for pop in ('first','second'):
    for key in vars(getattr(s0,pop)):
        assert np.array_equal(getattr(getattr(s0,pop),key),getattr(getattr(s1,pop),key))
assert np.array_equal(s0.D,s1.D)
assert all(not key.startswith('time') for key in vars(s0))
assert {record['population'] for record in program.diagnostics}=={1,2}

results = dict(status='PASS',inputs=inputs,guide_packet_correspondence=guide_sources,
    preserved_files=preserved,chapter_exact_single_insertion=True,frozen_CH1_exact=True,
    test_only_mechanical_adaptation=True,guide_changes=changes,new_links=new_links,
    module_import=str(Path(core.__file__).resolve()),
    supplied_state_gradient_max_errors=errors,
    independent_restarts=len(metadata_cases),carrier_permutation='PASS',
    rational_and_joint_observations='PASS',initialization_deterministic='PASS',
    python=sys.version,numpy=np.__version__,
    environment={k:os.environ.get(k) for k in ('PYTHONDONTWRITEBYTECODE','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','PYTHONPATH')})
(OUT/'independent_checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({key:value for key,value in results.items() if key not in ('inputs','guide_changes')},indent=2))
