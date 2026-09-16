"""Assemble this candidate into a fresh standalone edition, without live edits."""
import argparse
import shutil
from pathlib import Path

MAPPING = {
    'PROMOTION_observable_p1_initialization.py':'code/pde/observable_p1_initialization.py',
    'PROMOTION_observable_torch_p1.py':'code/pde/observable_torch_p1.py',
    'PROMOTION_finite_torch.py':'code/pde/finite_torch.py',
    'PROMOTION_closure_comparison.py':'code/pde/closure_comparison.py',
    'PROMOTION_test_general_p1.py':'code/tests/test_general_p1.py',
    'PROMOTION_example_general_p1.py':'code/scripts/example_general_p1.py',
    'PROMOTION_analyze_general_p1.py':'code/scripts/analyze_general_p1.py',
    'PROMOTION_THEORY.md':'docs/observable_p1.md',
    'PROMOTION_GUIDE.md':'code/GENERAL_P1.md',
}

def assemble(output):
    source=Path(__file__).resolve().parent
    root=source.parents[1]
    output=Path(output)
    output.mkdir(parents=True,exist_ok=False)
    # Full established docs/code are retained; only explicitly mapped candidate
    # files are added. No study history or generated arrays enter the edition.
    for name in ('docs','code'):
        shutil.copytree(root/name,output/name,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    for name,target in MAPPING.items():
        path=output/target;path.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source/name,path)
    with (output/'docs/README.md').open('a') as f:
        f.write('\n## General-dimension first-order implementation\n\n[General-d p=1 coefficients and finite computation](observable_p1.md) gives exact initialized coefficient and antithetic identities, a finite GPU backend and an actual-network comparator. It supplies no general-d trained-network convergence theorem or MNIST/PCA empirical conclusion.\n')
    with (output/'code/README.md').open('a') as f:
        f.write('\n## General-dimension p=1 and optional Torch comparator\n\nSee the [general-d p=1 guide](GENERAL_P1.md) for independent scalar initialization, complete finite tensor contractions, signed paired observations, restart, comparison methods and the bounded explicit-output example. Importing `pde` still requires only NumPy.\n')
    return output

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True,type=Path)
    print(assemble(parser.parse_args().output))
