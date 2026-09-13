from fractions import Fraction
from tempfile import TemporaryDirectory
from pathlib import Path
import hashlib,json,time,resource
import numpy as np
from pde.observable_solver import (initialize,ArcLaw,evolve,predict,circle_inputs,paired_observations,save_restart,load_restart,state_bytes)
from pde import observable_solver
started=time.process_time()
state=initialize(order=3,initialization_nodes=2048,population_nodes=1024)
data=ArcLaw().quadrature(nodes_per_arc=8,arithmetic=state.arithmetic)
final=evolve(state,data,steps=32,step_size=Fraction(1,6400))
directions=circle_inputs(128,final.arithmetic)
prediction=predict(final,directions)
observations=paired_observations(final,data)
print(observations['rms1'],observations['rms2'])
half=evolve(state,data,steps=16,step_size=Fraction(1,6400))
with TemporaryDirectory() as directory:
 checkpoint=Path(directory)/'observable_restart.json'
 save_restart(checkpoint,half,data)
 restored,restored_data=load_restart(checkpoint)
 checkpoint_sha256=hashlib.sha256(checkpoint.read_bytes()).hexdigest()
 continued=evolve(restored,restored_data,steps=16,step_size=Fraction(1,6400))
in_memory=evolve(half,data,steps=16,step_size=Fraction(1,6400))
keys=('b1','g','w','p1','b2','c','p2','M','D')
checks=dict(restart_equal_in_memory={k:bool(np.array_equal(getattr(continued,k),getattr(in_memory,k))) for k in keys},restart_equal_full={k:bool(np.array_equal(getattr(continued,k),getattr(final,k))) for k in keys},midpoint_roundtrip={k:bool(np.array_equal(getattr(half,k),getattr(restored,k))) for k in keys},data_roundtrip={k:bool(np.array_equal(getattr(data,k),getattr(restored_data,k))) for k in ('inputs','labels','probabilities')})
assert all(all(d.values()) for d in checks.values())
assert np.isfinite(prediction).all() and prediction.shape==(128,)
assert observations['first_pairs'].shape==observations['second_pairs'].shape==(1024,16,2)
result=dict(status='operational_pass',source=str(Path(observable_solver.__file__).resolve()),solver_sha256=hashlib.sha256(Path(observable_solver.__file__).read_bytes()).hexdigest(),checkpoint_sha256=checkpoint_sha256,checks=checks,rms1=float(observations['rms1']),rms2=float(observations['rms2']),prediction_max_abs=float(np.max(np.abs(prediction))),cpu_seconds=time.process_time()-started,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,state_bytes=state_bytes(final))
(Path(__file__).resolve().parent/'guide_example_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
