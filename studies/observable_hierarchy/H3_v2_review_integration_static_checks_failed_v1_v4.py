import ast, difflib, hashlib, importlib, json, os, re, resource, subprocess, sys, time
from pathlib import Path
started = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (120,120))
resource.setrlimit(resource.RLIMIT_AS, (4*1024**3,4*1024**3))
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
sys.dont_write_bytecode = True
scratch = Path(__file__).resolve().parent
repo = scratch.parents[3]
new = scratch.parent / 'H3_v2_edition_v3'
old = scratch.parent / 'H3_v2_edition_v2'
base = scratch.parent / 'H3_v2_integration_inputs_v3'
manifest = json.loads((new/'review/manifest.json').read_text())
integration = json.loads((repo/'studies/observable_hierarchy/H3_v2_integration_manifest_v4.json').read_text())
result = {'checks':{}}
changes=[]
for name in manifest['edition_hashes']:
    a=(old/name).read_bytes(); b=(new/name).read_bytes()
    if a!=b:
        changes.append(name)
        before=integration['presentation_correspondence']['before'].encode()
        after=integration['presentation_correspondence']['after'].encode()
        assert a.count(before)==b.count(after)==1
        assert a.replace(before,after)==b
assert sorted(changes)==sorted(integration['presentation_correspondence']['changed_files'])
result['checks']['edition_correspondence']=dict(changed=changes,byte_identical=27-len(changes))
section=(new/'review/proposed_section.md').read_text()
chapter=(new/'docs/global_nonlinear.md').read_text()
oldchapter=(base/'base_global_nonlinear.md').read_text()
assert chapter.count(section)==1
without=chapter.replace(section,'',1)
assert without==oldchapter or without.replace('\n\n\n','\n\n',1)==oldchapter
# Obtain exact inserted bytes, without allowing whitespace changes elsewhere.
match=difflib.SequenceMatcher(None,oldchapter.splitlines(True),chapter.splitlines(True),autojunk=False)
edits=[x for x in match.get_opcodes() if x[0]!='equal']
assert len(edits)==1 and edits[0][0]=='insert'
_,i,j,k,l=edits[0]
insert=''.join(chapter.splitlines(True)[k:l])
assert insert.strip()==section.strip()
result['checks']['chapter_insertion']=dict(base_offset_line=i+1,new_start=k+1,new_end=l,only_section_and_separator=True)
guide=(new/'review/library_guide.md').read_text()
codeguide=(new/'code/README.md').read_text(); codebase=(base/'base_code_README.md').read_text()
assert codeguide.startswith(codebase)
assert codeguide[len(codebase):].strip()==re.sub(r'^(#+)',r'\1#',guide,flags=re.M).strip()
result['checks']['code_guide_preservation']='exact prefix; appended complete guide with heading depth +1'
docsbase=(base/'base_docs_README.md').read_text(); docsguide=(new/'docs/README.md').read_text()
diff=''.join(difflib.unified_diff(docsbase.splitlines(True),docsguide.splitlines(True),fromfile='frozen base',tofile='reviewed edition'))
(scratch/'roadmap.diff').write_text(diff)
# Match complete source paragraphs against the frozen full chapters, retaining
# source locations without displaying any unassigned scientific complement.
dependency=(new/'review/dependencies.md').read_text()
boundaries=list(re.finditer(r'^Source: `([^`]+)`;.*$',dependency,re.M))
scope=[]
for index,boundary in enumerate(boundaries):
    start=boundary.end()+2
    end=boundaries[index+1].start() if index+1<len(boundaries) else len(dependency)
    body=dependency[start:end].strip()
    if body.endswith('---'):body=body[:-3].rstrip()
    source=(new/boundary.group(1)).read_text()
    if body in source:
        offset=source.index(body); lo=source[:offset].count('\n')+1
        scope.append(dict(packet_heading=boundary.group(),source_start=lo,source_end=lo+body.count('\n'),exact=True))
    else:
        # Selections that concatenate several full proof parts need multiple
        # exact blocks; all nonempty nonseparator packet lines must match.
        s1=body.splitlines();s2=source.splitlines()
        blocks=difflib.SequenceMatcher(None,s1,s2,autojunk=False).get_matching_blocks()
        covered={i for block in blocks for i in range(block.a,block.a+block.size)}
        omitted=[(i+1,x) for i,x in enumerate(s1) if i not in covered and x.strip() and x.strip()!='---']
        assert not omitted, omitted
        scope.append(dict(packet_heading=boundary.group(),exact=True,source_blocks=[(b.b+1,b.b+b.size) for b in blocks if b.size]))
result['checks']['selected_source_correspondence']=scope
sys.path.insert(0,str(new/'code'))
imports={}
for name in manifest['edition_hashes']:
    if not name.endswith('.py'):continue
    tree=ast.parse((new/name).read_text(),filename=name)
    imports[name]=[dict(module=n.module,level=n.level,names=[a.name for a in n.names]) if isinstance(n,ast.ImportFrom)
                   else dict(names=[a.name for a in n.names]) for n in ast.walk(tree) if isinstance(n,(ast.Import,ast.ImportFrom))]
for name in ('finite_network','gaussian_moments','observable_closure','observable_fixed','observable_arithmetic','observable_words','observable_compiler','observable_initialization','observable_solver'):
    mod=importlib.import_module('pde.'+name)
    assert Path(mod.__file__).resolve()==(new/'code/pde'/f'{name}.py').resolve()
result['checks']['ast_and_imports']=imports
import markdown
raw_html=markdown.markdown(section,extensions=['fenced_code','tables'])
assert '<a ' not in raw_html
expressions=list(re.finditer(r'\\\[(.*?)\\\]|\\\((.*?)\\\)',section,re.S))
assert len(expressions)==331
assert section.count('\\[')==section.count('\\]')==80
assert section.count('\\(')==section.count('\\)')==251
tex=['\\documentclass{article}','\\usepackage{amsmath,amssymb,mathtools}','\\begin{document}']
for index,m in enumerate(expressions,1):
    tex.append('Expression '+str(index)+' (source line '+str(section[:m.start()].count('\n')+1)+').')
    tex.append(m.group())
    tex.append('\\par\\medskip')
tex.append('\\end{document}')
(scratch/'section_math.tex').write_text('\n'.join(tex)+'\n')
result['checks']['math']=dict(display=80,inline=251,accidental_links=0,tex_artifact='section_math.tex')
heading=re.search(r'^##### (C\.4\.7\.10\..*)$',section,re.M).group(1)
slug=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-')
target='global_nonlinear.md#'+slug
assert '[C.4.7.10]('+target+')' in docsguide
assert chapter.count('##### '+heading)==1
oldlinks=set(re.findall(r'\]\(([^)]+)\)',docsbase))
newlinks=set(re.findall(r'\]\(([^)]+)\)',docsguide))
assert newlinks-oldlinks=={target}
assert not re.findall(r'\]\(([^)]+)\)',guide)
result['checks']['new_links']=dict(roadmap=target,unique_heading=True,section_links=[],library_guide_links=[])
result['cpu_seconds']=time.process_time()-started
result['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
(scratch/'static_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
print(json.dumps({k:v for k,v in result['checks'].items() if k!='ast_and_imports'},indent=2))
