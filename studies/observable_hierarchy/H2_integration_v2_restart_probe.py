"""Static round-trip for an ordinary finite supplied state; no evolution."""
from pathlib import Path
import json
from pde import observable_closure as closure

scratch = Path('/home/amir/Codes/PDE/data/generated/observable_hierarchy/H2_integration_v2')
state = closure.State(
    closure.Population1([[1.]], [[0., 0.]], [[1., 0.]], [1.]),
    closure.Population2([[1.]], [0.2], [1.]),
    [[0.3]], [[0.3]],
)
data = closure.DataLaw([[1., 0.]], [1.], [1.])
record = {'metadata': state.metadata,
          'loss': closure.loss(state, data),
          'rhs_M': closure.rhs(state, data).M.tolist()}
path = scratch / 'supplied_restart.npz'
closure.save_restart(path, state, data)
record['save_succeeded'] = True
try:
    restored, restored_data = closure.load_restart(path)
    record['load_succeeded'] = True
except ValueError as error:
    record['load_succeeded'] = False
    record['load_error'] = str(error)
(scratch / 'supplied_restart_result.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
