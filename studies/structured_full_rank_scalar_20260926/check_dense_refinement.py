"""Compare matched coarse/fine dense trajectories without risk model selection."""
import argparse,json
from pathlib import Path
import numpy as np


def main():
    p=argparse.ArgumentParser()
    p.add_argument("coarse");p.add_argument("fine");p.add_argument("--output",required=True)
    a=p.parse_args();coarse=Path(a.coarse);fine=Path(a.fine)
    def load(root):
        result={}
        for path in root.glob("*__dt*.json"):
            rec=json.loads(path.read_text())
            result[(rec["task"],rec["width"],rec["seed"],rec["method"])]=rec
        return result
    left,right=load(coarse),load(fine)
    rows=[];passed=True
    for key in sorted(set(left)|set(right)):
        l,r=left.get(key),right.get(key)
        row={"task":key[0],"width":key[1],"seed":key[2],"method":key[3]}
        if not l or not r or l["status"]!="ok" or r["status"]!="ok":
            row.update(passed=False,error="missing or failed paired run")
            rows.append(row);passed=False;continue
        scale=l["target_rms"]
        with np.load(coarse/l["data_file"]) as la,np.load(fine/r["data_file"]) as ra:
            diffs={}
            for stage in l["records"].keys()&r["records"].keys():
                rms=float(np.sqrt(np.mean((la[stage+"_circle"]-ra[stage+"_circle"])**2)))/scale
                risk=abs(l["records"][stage]["test_rms"]-r["records"][stage]["test_rms"])/scale
                diffs[stage]={"function_rms_over_target":rms,"risk_delta_over_target":risk}
        valid=(l["fitted"]==r["fitted"] and l["max_loss_rise"]<=1e-7 and
               r["max_loss_rise"]<=1e-7 and all(v["function_rms_over_target"]<=.002 and
               v["risk_delta_over_target"]<=.001 for v in diffs.values()))
        grid=max(v["grid_refinement_delta"]/scale for rec in (l,r) for v in rec["records"].values())
        valid=valid and grid<=1e-4
        row.update(passed=valid,stages=diffs,grid_delta_over_target=grid,
                   coarse_fitted=l["fitted"],fine_fitted=r["fitted"])
        rows.append(row);passed=passed and valid
    result={"passed":passed,"pairs":len(rows),"rows":rows,
            "maximum_function_rms_over_target":max((v["function_rms_over_target"] for row in rows for v in row.get("stages",{}).values()),default=None),
            "maximum_risk_delta_over_target":max((v["risk_delta_over_target"] for row in rows for v in row.get("stages",{}).values()),default=None)}
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="rows"}))
    for row in rows:
        if not row["passed"]: print(json.dumps(row))


if __name__=="__main__":main()
