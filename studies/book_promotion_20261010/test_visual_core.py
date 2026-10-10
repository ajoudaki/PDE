"""Tiny geometry, plot-contract and executable offline-viewer checks."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from visual_core import plot_circle, plot_sphere, radial_coordinates, sphere_projection, write_viewer


class VisualCoreTests(unittest.TestCase):
    def setUp(self):
        self.circle = np.array([[1., 0.], [0., 1.], [-1., 0.], [0., -1.]])
        self.sphere = np.array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.],
                                [0., 0., -1.], [.6, 0., -.8]])

    def tearDown(self):
        plt.close('all')

    def test_signed_radial_geometry_never_folds(self):
        values = np.array([-2., 0., 2., -1.])
        xy = radial_coordinates(self.circle, values, limit=2.)
        np.testing.assert_allclose(np.linalg.norm(xy, axis=1), [.2, 1., 1.8, .6])
        np.testing.assert_allclose(xy / np.linalg.norm(xy, axis=1)[:, None], self.circle)
        for limit in (0., -1., 1., np.inf):
            with self.assertRaises(ValueError):
                radial_coordinates(self.circle, values, limit=limit)

    def test_sphere_complement_and_camera_axes(self):
        front, a = sphere_projection(self.sphere)
        back, b = sphere_projection(self.sphere, back=True)
        self.assertTrue(np.all(a ^ b))
        np.testing.assert_array_equal(a, [True, True, True, False, False])
        np.testing.assert_allclose(front, self.sphere[:, :2])
        np.testing.assert_allclose(back, self.sphere[:, :2] * [-1., 1.])
        self.assertTrue(np.all(np.linalg.norm(front, axis=1) <= 1.))

    def test_shapes_finiteness_and_frame_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'viewer.html'
            bad_cases = [dict(predictions={}), dict(predictions={'x': [1, 2, 3]}),
                         dict(predictions={'x': [0, 0, np.nan, 0]}),
                         dict(predictions={'x': np.zeros((2, 4)), 'y': np.zeros(4)}),
                         dict(predictions={'x': np.zeros((2, 4))}, times=[1, 0]),
                         dict(predictions={'x': np.zeros(4)}, reference='missing'),
                         dict(predictions={'x': np.zeros(4)}, training_labels=[1.])]
            for kwargs in bad_cases:
                with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                    write_viewer(path, self.circle, **kwargs)
            with self.assertRaises(ValueError):
                write_viewer(path, self.circle * 2, {'x': np.zeros(4)})
        for frame in (2, -3, 1.2, True):
            with self.assertRaises(ValueError):
                plot_circle(self.circle, {'x': np.zeros((2, 4))}, frame=frame)

    def test_circle_zero_ring_and_common_range(self):
        values = {'reference': np.array([[0., 0., 0., 0.], [2., -2., 0., 0.]]),
                  'model': np.array([[1., 0., -1., 0.], [1., -1., 0., 0.]])}
        fig = plot_circle(self.circle, values, reference='reference', frame=0,
                          training_inputs=self.circle[:1], training_labels=[4.])
        self.assertEqual(len(fig.axes), 2)
        # Later frames and training labels establish the common prediction scale 4.
        radii = np.linalg.norm(np.column_stack(fig.axes[0].lines[1].get_data()), axis=1)
        np.testing.assert_allclose(sorted(radii), [.8, 1., 1., 1., 1.2])
        zero_rings = [p for p in fig.axes[0].patches if p.get_linestyle() == '--']
        self.assertEqual(len(zero_rings), 1)
        self.assertEqual(zero_rings[0].radius, 1.)
        self.assertIn('sampled RMS', fig.axes[1].get_legend().get_texts()[0].get_text())

    def test_sphere_signed_errors_and_scales(self):
        ref = np.zeros((2, 5))
        model = np.array([[1., -2., 3., -4., 5.], [-6., 0., 0., 0., 0.]])
        fig = plot_sphere(self.sphere, {'ref': ref, 'model': model}, frame=0,
                          model='model', reference='ref', training_inputs=self.sphere[:1])
        main = fig.axes[:6]
        for axis in main:
            self.assertEqual(axis.collections[0].get_clim(), (-6., 6.))
        np.testing.assert_allclose(main[2].collections[0].get_array(), [1., -2., 3.])
        np.testing.assert_allclose(main[5].collections[0].get_array(), [-4., 5.])
        self.assertEqual(main[3].get_xlabel(), '−x (view from −z)')
        self.assertIn('sampled RMS', main[2].get_title())
        for colorbar in fig.axes[6:]:
            np.testing.assert_allclose(colorbar.get_xticks(), [-6., 0., 6.])

    def test_html_escaping_and_fixed_scales(self):
        hostile = '</script><img src=x onerror=alert(1)>&\u2028'
        with tempfile.TemporaryDirectory() as directory:
            path = write_viewer(Path(directory) / 'view.html', self.circle,
                                {hostile: np.zeros((2, 4)), 'other': np.array([[1., -1., 0., 0.], [8., 0., 0., 0.]])},
                                title=hostile, times=[0., .1])
            source = path.read_text()
        self.assertNotIn(hostile, source)
        self.assertEqual(source.count('</script>'), 2)
        self.assertNotRegex(source, r'(?:src|href)=["\']https?://')
        data = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', source, re.S)[1])
        self.assertEqual(data['names'][0], hostile)
        self.assertEqual(data['scale'], 8.)
        self.assertEqual(data['error_scale'], 8.)

    @unittest.skipUnless(shutil.which('node'), 'Node is needed for executable browser-control checks')
    def test_offline_javascript_updates_models_frames_and_reference(self):
        # A minimal DOM/canvas implements the API used by the actual embedded
        # script, so this runs its listeners and metric computation, not a port.
        harness = r'''
const fs=require('fs'), assert=require('assert'), vm=require('vm');
const html=fs.readFileSync(process.argv[1],'utf8');
const scripts=[...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(x=>x[1]);
let draws=0;
const ctx=new Proxy({}, {get:(o,k)=>o[k]??(()=>{draws++;}),set:(o,k,v)=>(o[k]=v,true)});
function element(){return {value:'0',textContent:'',children:[],listeners:{},
 appendChild(x){this.children.push(x);},setAttribute(){},getContext(){return ctx;},
 addEventListener(k,f){this.listeners[k]=f;}};}
const ids={}; for(const id of ['data','title','description','model','reference','frame','clock','time','play','plots','metrics'])ids[id]=element();
ids.data.textContent=scripts[0];
const document={getElementById:id=>ids[id],createElement:element,addEventListener(){},hidden:false};
vm.runInNewContext(scripts[1],{document,setInterval:()=>1,clearInterval(){},console});
assert(ids.metrics.textContent.includes('sampled RMS 1.000'));
const initialDraws=draws; ids.frame.value='1';ids.frame.listeners.input();
assert(ids.metrics.textContent.includes('time 0.1000'));
assert(ids.metrics.textContent.includes('sampled RMS 2.000'));
assert(draws>initialDraws);
ids.model.value='0';ids.model.listeners.input();assert(ids.metrics.textContent.includes('sampled RMS 0.000'));
ids.reference.value='1';ids.reference.listeners.input();assert(ids.metrics.textContent.includes('sampled RMS 2.000'));
assert(ids.metrics.textContent.includes('reference versus model'));
ids.play.listeners.click();assert.equal(ids.play.textContent,'Pause');ids.play.listeners.click();assert.equal(ids.play.textContent,'Play');
console.log('offline controls and canvas redraw passed');
'''
        with tempfile.TemporaryDirectory() as directory:
            for q in (self.circle, self.sphere):
                path = write_viewer(Path(directory) / 'view.html', q,
                                    {'reference': np.zeros((2, len(q))),
                                     'model': np.array([np.ones(len(q)), 2 * np.ones(len(q))])}, times=[0., .1])
                result = subprocess.run(['node', '-e', harness, str(path)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
