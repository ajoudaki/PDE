"""Preselected input-geometry extension for the fixed selective scalar ODE.

These tasks reuse the study's odd teachers and canonical circle convention.
No task or initialization seed is chosen after viewing the new results.
"""
import numpy as np
from circle_tasks import Task, BY_NAME as EXISTING

TASKS = (
    EXISTING['pair_cos3'],
    EXISTING['near_pair_sin9'],
    Task('pair_orthogonal_cos1', (0., np.pi/2), 'cos1'),
    EXISTING['triple_cos3'],
    Task('cluster_triple_cos1', (-np.pi/9, 0., np.pi/9), 'cos1'),
    Task('triple_wide_mixed', (.13, 2.10, 4.19), 'mixed'),
    Task('quartet_broad', (.05, .70, 1.65, 2.65), 'broad'),
    Task('quartet_mixed', (.13, .85, 1.72, 2.60), 'mixed'),
)
BY_NAME = {task.name: task for task in TASKS}
TASK_NAMES = tuple(BY_NAME)

def manifest():
    return [dict(name=task.name, angles=list(task.angles),
                 teacher=task.teacher,
                 labels=task.target(task.angles).tolist()) for task in TASKS]
