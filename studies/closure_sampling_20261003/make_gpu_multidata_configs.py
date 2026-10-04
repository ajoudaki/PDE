"""Persist fixed data and the preregistered main configs; no training."""
from pathlib import Path
import json
import numpy as np

HERE = Path(__file__).resolve().parent


def unit_gaussian(count, dimension, seed):
    values = np.random.default_rng(seed).normal(size=(count, dimension))
    return values / np.linalg.norm(values, axis=1)[:, None]


def circle(theta):
    return np.column_stack((np.cos(theta), np.sin(theta)))


def query_panel(d, refined=False):
    if d == 2:
        size = 514 if refined else 257
        offset = 1. if refined else .5
        return circle(2*np.pi*(np.arange(size)+offset)/size)
    return unit_gaussian(1024 if refined else 512, d, 9600+d)


def datasets():
    result = {}
    def add(name, U, y, group, description):
        U, y = np.asarray(U), np.asarray(y)
        d, m = U.shape[1], len(U)
        pair = U @ U.T
        np.fill_diagonal(pair, 0.)
        assert np.max(np.abs(pair)) < 1-1e-10
        assert np.allclose(np.linalg.norm(U, axis=1), 1.)
        setup = circle(np.pi*np.arange(32)/32) if d == 2 else unit_gaussian(32,d,9500+d)
        result[name] = dict(U=U.tolist(), labels=y.tolist(),
            setup_probes=setup.tolist(), query_panel=query_panel(d).tolist(),
            description=description, metadata=dict(group=group, dimension=d,
                sample_count=m, max_abs_offdiagonal_input_gram=float(np.max(np.abs(pair))),
                input_rank=int(np.linalg.matrix_rank(U)),
                label_rms=float(np.sqrt(np.mean(y*y))), query_seed=9600+d,
                setup_seed=None if d==2 else 9500+d))
    pair = circle(np.deg2rad([0,15]))
    add('circle2_close_same',pair,[.1,.1],'close_pairs','15-degree pair, equal positive labels')
    add('circle2_close_opposite',pair,[.1,-.1],'close_pairs','15-degree pair, opposite equal labels')
    theta4 = np.deg2rad(7)+np.arange(4)*np.pi/4
    theta8 = np.deg2rad(7)+np.arange(8)*np.pi/8
    U4, U8 = circle(theta4), circle(theta8)
    y4 = .15*np.cos(theta4)+.05*np.sin(theta4)
    y8 = .15*np.cos(theta8)+.05*np.sin(theta8)
    add('circle4_smooth',U4,y4,'multi_circle','Four nonantipodal directions, first harmonic')
    add('circle4_harmonic',U4,.15*np.cos(3*theta4),'multi_circle','Four directions, third harmonic')
    add('circle8_smooth',U8,y8,'multi_circle','Eight nonantipodal directions, first harmonic')
    add('circle8_harmonic',U8,.15*np.cos(theta8)+.05*np.sin(3*theta8),'multi_circle','Eight directions, first plus third harmonic')
    for d in (3,5):
        add(f'embedded_circle8_d{d}',np.pad(U8,((0,0),(0,d-2))),y8,
            f'embedded_d{d}',f'Same eight-point circle embedded in dimension{d}, full sphere queries')
    tetra = np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/np.sqrt(3)
    add('sphere3_tetra4',tetra,[.15,-.1,.1,-.15],'sphere_d3','Four tetrahedron vertices')
    for d in (3,5):
        U = unit_gaussian(8,d,9108)
        add(f'sphere{d}_eight_smooth',U,.15*U[:,0]+.05*U[:,1],
            f'sphere_d{d}','Eight fixed general-position directions, linear sphere labels')
    U = np.array(result['sphere3_eight_smooth']['U'])
    add('sphere3_eight_nonlinear',U,.15*U[:,0]+.15*np.prod(U,axis=1),
        'sphere_d3','Same eight directions, linear plus cubic odd labels')
    assert len(result)==12
    return result


def main():
    data=datasets()
    # Alternate configs across GPUs to mix long circle and sphere trajectories.
    names=list(data)
    for worker in (0,1):
        assigned=names[worker::2]
        config=dict(description='Frozen multidata baseline; no budget increase',
            stage='baseline', protocol='studies/closure_sampling_20261003/GPU_MULTIDATA_PROTOCOL.md',
            datasets={k:data[k] for k in assigned},
            cases=[dict(dataset_id=k,n=n,seed=s) for n in (512,1024,2048)
                   for s in (9411,9412) for k in assigned],
            samplers=[dict(name='budget1_rank16',coefficient_multiplier=1.,rank=16)],
            dt=.2,observe_every=1.,horizon=120.,max_horizon=1200.,
            settlement_every=120.,tail_window=10.,fit_tolerance=1e-6,
            settlement_tolerance=1e-5,budget_seconds=900.,max_allocation_gib=8.,
            dtype='float64',mass_floor=.05,
            source_files=['studies/closure_sampling_20261003/GPU_MULTIDATA_PROTOCOL.md',
                          'studies/closure_sampling_20261003/make_gpu_multidata_configs.py'])
        target=HERE/f'gpu_multidata_baseline_{worker}.json'
        if target.exists():
            raise FileExistsError(target)
        target.write_text(json.dumps(config,indent=2,allow_nan=False)+'\n')
        print(target)


if __name__=='__main__':
    main()
