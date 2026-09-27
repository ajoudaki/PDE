"""Frozen odd circle teachers and finite training designs for dense comparison."""
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Task:
    name: str
    angles: tuple
    teacher: str

    def target(self, angles):
        a = np.asarray(angles)
        if self.teacher.startswith("cos"):
            return np.cos(int(self.teacher[3:]) * a)
        if self.teacher.startswith("sin"):
            return np.sin(int(self.teacher[3:]) * a)
        if self.teacher == "mixed":
            return .6*np.cos(a) + .25*np.sin(3*a) + .15*np.cos(7*a)
        if self.teacher == "broad":
            return np.tanh(3*np.cos(a-.35))
        if self.teacher == "sharp":
            return np.tanh(10*np.cos(a-.37))
        raise ValueError(self.teacher)

    def data(self):
        a = np.asarray(self.angles)
        return directions(a), self.target(a)


def directions(angles):
    a = np.asarray(angles)
    return np.column_stack((np.cos(a), np.sin(a)))


TASKS = (
    Task("pair_cos1", (0., .9), "cos1"),
    Task("pair_cos3", (0., np.pi/3), "cos3"),
    Task("near_pair_sin9", (-np.pi/18, np.pi/18), "sin9"),
    Task("triple_cos3", (0., np.pi/5, -np.pi/5), "cos3"),
    Task("triple_mixed", (.13, 1.02, 2.41), "mixed"),
    Task("cluster_triple_cos9", (-np.pi/9, 0., np.pi/9), "cos9"),
    Task("broad_ridge6", (0., .22, .8, 1.45, 2.23, 2.9), "broad"),
    Task("sharp_ridge8", tuple(.07+np.arange(8)*np.pi/8), "sharp"),
    Task("alternating3", tuple(np.arange(6)*np.pi/3), "cos3"),
    Task("alternating5", tuple(np.arange(10)*np.pi/5), "cos5"),
    Task("alternating9", tuple(np.arange(18)*np.pi/9), "cos9"),
    Task("multiscale12", (.03,.24,.61,.94,1.19,1.66,1.92,2.21,2.58,2.83,3.07,4.31), "mixed"),
)
BY_NAME = {task.name: task for task in TASKS}
METHODS = ("gaussian", "gaussian_control", "hd", "hdhd", "fastfood", "reflection4", "diagonal")


def task_manifest():
    return [{"name": t.name, "angles": list(t.angles), "teacher": t.teacher,
             "labels": t.target(t.angles).tolist()} for t in TASKS]
