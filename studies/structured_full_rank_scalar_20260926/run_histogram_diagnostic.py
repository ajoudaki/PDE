"""Complete the two planned histograms with the unresolved reference labelled.

This preserves the failed reference gate. It cannot authorize extra tasks,
additional reference fits, or a clean-pass claim.
"""
import argparse
import json
from pathlib import Path
import shutil
import sys
import numpy as np
from run_histogram_candidate import GRIDS, run_histogram, digest, write


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();out=args.output.resolve()
    old=json.loads((out/'manifest.json').read_text())
    rows=json.loads((out/'results.json').read_text())
    assert len(rows)==3 and all(r['kind']=='reference' for r in rows)
    assert digest(out/'histogram_one_input.so')==old['library_sha256']
    check=json.loads((out/'reference_check.json').read_text())
    assert not check['passed']
    selected=next(r for r in rows if r['gaussian_seed_order']==check['selected_order'])
    assert digest(out/selected['data_file'])==selected['data_sha256']
    with np.load(out/selected['data_file']) as data:reference=data['prediction']
    source=Path(__file__).resolve().parent
    for name,h in old['sources'].items():assert digest(source/name)==h
    shutil.copyfile(out/'decision.json',out/'initial_reference_stop.json')
    shutil.copyfile(__file__,out/'source_snapshot'/Path(__file__).name)
    write(out/'diagnostic_manifest.json',{'command':sys.argv,'source_sha256':digest(__file__),
          'reference_status':'unresolved; gate remains failed','reference_check':check,
          'authorized_runs':'two originally planned histograms; no expansion or further references'})
    for name,shape in GRIDS.items():
        row,prediction=run_histogram(out/'histogram_one_input.so',out,name,shape,reference)
        rows.append(row);write(out/'results.json',rows)
    write(out/'decision.json',{'passed':False,'status':'diagnostic only',
        'reason':'reference refinement exceeded its predeclared gate',
        'next_action':'stop; no additional tasks or training runs'})


if __name__=='__main__':main()
