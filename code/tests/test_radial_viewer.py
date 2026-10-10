"""Execute the real offline application and D3, with a small DOM/SVG stand-in."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from pde.radial_explorer import write_explorer


HARNESS = r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync(process.argv[1],'utf8');
const scripts=[...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(x=>x[1]);
class Element {
 constructor(tag='div'){this.tag=tag;this.children=[];this.listeners={};this.dataset={};this.style={};this.value='';this.textContent='';}
 append(...xs){this.children.push(...xs);} replaceChildren(...xs){this.children=xs;}
 setAttribute(k,v){this[k]=v;} addEventListener(k,f){this.listeners[k]=f;}
 get options(){return this.children.flatMap(c=>c.tag==='optgroup'?c.children:[c]);}
 get selectedOptions(){return this.options.filter(c=>c.value===this.value);}
 getBoundingClientRect(){return {width:700,top:0,left:0};}
 async fire(k){await this.listeners[k]();}
}
const roles={};for(const m of html.matchAll(/data-role="([^"]+)"/g))roles[m[1]]=new Element();
const root=new Element();root.querySelector=s=>roles[s.match(/data-role="([^"]+)"/)[1]];
for(const [v,t] of [['time','Time'],['loss','Loss'],['settled','Recorded endpoints']]){const o=new Element('option');o.value=v;o.textContent=t;roles.alignment.append(o);}
roles.alignment.value='time';roles.view.value='radial';roles.progress.value='0';roles.payload.textContent=scripts[0];
const document={getElementById:()=>root,createElement:t=>new Element(t),createTextNode:t=>({textContent:t}),addEventListener(){}};
const selections=[];
class Selection {
 constructor(){this.attrs={};this.listeners={};selections.push(this);}
 selectAll(){return this;} data(){return this;} join(){return this;} remove(){return this;}
 append(){return new Selection();} select(){return new Selection();}
 attr(k,v){this.attrs[k]=v;return this;} text(){return this;} call(){return this;}
 on(k,f){this.listeners[k]=f;return this;} node(){return {};}
}
const context=vm.createContext({document,console,matchMedia:()=>({matches:false}),
 requestAnimationFrame:()=>1,cancelAnimationFrame(){},ResizeObserver:class{observe(){}}});
vm.runInContext(scripts[1],context); // Actual bundled D3 numerical/path routines.
context.d3.select=()=>new Selection();context.d3.pointer=e=>[e.x,e.y];
vm.runInContext(scripts[2],context);
function good(){assert(roles.error.hidden,roles.error.textContent);}
function check(){good();return root.__viewerCheck();}
function close(x,y){assert(Math.abs(x-y)<1e-8,`${x} != ${y}`);}
(async()=>{
 if(process.argv[2]==='smoke'){
   assert.equal(root.dataset.ready,'true');
   for(const c of JSON.parse(scripts[0]).cases){
     roles.experiment.value=c.id;await roles.experiment.fire('change');good();
     for(const mode of ['settled','time','loss']){
       if(roles.alignment.options.find(o=>o.value===mode).disabled)continue;
       roles.alignment.value=mode;roles.progress.value='500';await roles.alignment.fire('change');good();
     }
   }
   console.log('All supplied example cases initialized and rendered in each available alignment mode.');return;
 }
 assert.equal(root.dataset.ready,'true');assert.equal(root.dataset.experimentCount,2);
 assert.equal(check().networkId,'n32');
 roles.width.value='64';await roles.width.fire('change');assert.equal(check().networkId,'n64a');
 roles.seed.value='n64b';await roles.seed.fire('change');assert.equal(check().networkId,'n64b');
 roles.progress.value='500';await roles.progress.fire('input');
 let state=check();close(state.states[0].time,1);close(state.states[0].loss,.25);close(state.states[0].curve[0],.5);
 // MSE(interpolated prediction)=.25, not interpolation of the scalar MSE=.5.
 const radius=state.radius;roles.progress.value='0';await roles.progress.fire('input');close(check().radius,radius);
 roles.alignment.value='loss';roles.progress.value='500';await roles.alignment.fire('change');
 state=check();close(state.states[0].loss,state.states[1].loss);assert.notEqual(state.states[0].time,state.states[1].time);
 roles.alignment.value='settled';await roles.alignment.fire('change');assert(roles['slider-wrap'].hidden);assert(roles['sampling-note'].textContent.includes('not inferred'));
 roles.view.value='angle';await roles.view.fire('change');good();
 const paths=selections.filter(s=>s.attrs['data-curve']);assert(paths.length);assert(paths.every(s=>!s.attrs.d.includes('NaN')));
 // Hover at angle zero exercises interpolation across a nonzero-phase query grid.
 const hit=selections.filter(s=>s.attrs['data-chart-hit']!==undefined).at(-1);
 hit.listeners.pointermove({x:66,y:100});assert.equal(roles.tooltip.hidden,false);
 close(Number(roles.tooltip.children[1].children[1].textContent),2); // mean of endpoints 3 and 1.
 const toggle=roles.legend.children.find(b=>b.dataset.model==='method:method');await toggle.fire('click');assert.equal(check().states.length,1);
 await toggle.fire('click');assert.equal(check().states.length,2);
 roles.experiment.value='single';await roles.experiment.fire('change');good();assert(roles['network-controls'].hidden);
 roles.alignment.value='time';await roles.alignment.fire('change');close(check().states[0].time,3);
 roles.experiment.value='pair';await roles.experiment.fire('change');good();
 const original=JSON.parse(scripts[0]).cases[0];
 const fresh=JSON.parse(JSON.stringify(original));fresh.id='loaded';fresh.label='Loaded';
 roles.files.files=[{text:async()=>JSON.stringify(fresh)},{text:async()=>JSON.stringify({cases:[{...fresh,id:'another'}]})}];
 await roles.files.fire('change');assert.equal(root.dataset.experimentCount,4);assert.equal(check().caseId,'loaded');
 const malformed=JSON.parse(JSON.stringify(fresh));malformed.id='bad';malformed.models[0].losses=[123,0];
 roles.files.files=[{text:async()=>JSON.stringify(malformed)}];await roles.files.fire('change');assert.equal(root.dataset.experimentCount,4);assert(!roles.error.hidden);
 roles.files.files=[{text:async()=>JSON.stringify(fresh)}];await roles.files.fire('change');assert.equal(root.dataset.experimentCount,4);assert(!roles.error.hidden);
 const disjoint=JSON.parse(JSON.stringify(original));disjoint.id='disjoint';disjoint.models.at(-1).times=[4,8];disjoint.models.at(-1).finalTime=8;
 roles.files.files=[{text:async()=>JSON.stringify(disjoint)}];await roles.files.fire('change');assert.equal(check().mode,'settled');assert(roles.alignment.options.find(o=>o.value==='time').disabled);
 await roles.clear.fire('click');assert.equal(root.dataset.experimentCount,0);assert.equal(root.__viewerCheck().caseId,null);
 console.log('Experiment/width/seed switches, time and loss alignment, endpoint semantics, angular wrap, toggles, atomic multi-file import, malformed losses, duplicate IDs, disjoint ranges and clear passed.');
})().catch(e=>{console.error(e);process.exitCode=1;});
'''


def _test_scratch():
    import os
    root = Path(os.environ.get('PDE_OPTIONAL_TEST_SCRATCH',
                               Path(__file__).resolve().parents[2] / 'data/established/optional_tests'))
    root.mkdir(parents=True, exist_ok=True)
    return root



class RadialViewerTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which('node'), 'Node required for real viewer-script checks')
    def test_controls_and_alignment(self):
        def model(ident, end=2, **metadata):
            return dict(id=ident, times=[0, end], curves=[[0, 0, 0, 0], [1, 2, 2, 3]],
                        trainPredictions=[[0, 0], [1, 1]], **metadata)
        case = dict(id='pair', label='Pair', anglesDegrees=[0, 180], labels=[1, 1],
                    weights=[.25, .75], queryAnglesDegrees=[45, 135, 225, 315], models=[
                        model('n32', kind='network', width=32, seed=1),
                        model('n64a', kind='network', width=64, seed=1),
                        model('n64b', kind='network', width=64, seed=2), model('method', end=4)])
        single = dict(id='single', label='Single frame', anglesDegrees=[0], labels=[1],
                      models=[dict(id='one', times=[3], curves=[[1, 1, 1]], trainPredictions=[[1]])])
        with tempfile.TemporaryDirectory(dir=_test_scratch()) as directory:
            path = write_explorer(Path(directory)/'explorer.html', {'cases': [case, single]})
            result = subprocess.run(['node', '-e', HARNESS, str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
