from pathlib import Path
import json,subprocess,os,re,sys,hashlib,time
r=Path(__file__).resolve().parents[1];s=r/'integration_reviewer';e=r/'edition'
env=dict(os.environ,PYTHONPATH=str(e/'code'),PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
commands=[('imports',[sys.executable,'-B','-c',"import pde,pde.mfp_compiler,pde.mfp_expr,pde.mfp_finite; print(pde.__file__); assert 'Program' not in pde.__all__"]),('boundary',[sys.executable,'-B','code/tools/check_library.py']),('calculus',[sys.executable,'-B','code/scripts/example_mfp_calculus.py']),('mlp',[sys.executable,'-B','code/scripts/example_mfp_mlp_derivative.py']),('producer',[sys.executable,'-B','code/scripts/example_mfp_kernel_jets.py','--activation','all','--output-dir',str(s/'producer')])]
for i,body in enumerate(re.findall(r'```python\n(.*?)```',(e/'code/MFP_CALCULUS.md').read_text(),re.S),1):commands.append((f'guide_{i}',[sys.executable,'-B','-c',body]))
commands.append(('book_code',[sys.executable,'-B','-c',re.findall(r'```python\n(.*?)```',(r/'review_packet/promotion_theory.qmd').read_text(),re.S)[0]]))
results=[]
for name,cmd in commands:
 start=time.monotonic();p=subprocess.run(cmd,cwd=e,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT);(s/(name+'.log')).write_text(p.stdout);results.append(dict(name=name,command=cmd,cwd=str(e),exit_code=p.returncode,seconds=time.monotonic()-start));print(name,p.returncode,flush=True)
(s/'interface_commands.json').write_text(json.dumps(results,indent=2)+'\n')
original=e/'data/established/mfp_kernel_jets_01';fresh=s/'producer';hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in fresh.iterdir() if p.suffix in ('.txt','.json') and p.name!='manifest.json'}
comparison={name:hashlib.sha256((original/name).read_bytes()).hexdigest()==h for name,h in hashes.items()};(s/'producer_comparison.json').write_text(json.dumps(dict(output_sha256=hashes,equal_to_standalone_validation=comparison),indent=2)+'\n');print('producer comparison',comparison)
