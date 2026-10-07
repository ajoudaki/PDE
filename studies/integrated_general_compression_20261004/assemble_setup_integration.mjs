// Faithful, study-scoped import of the checked initialization arguments.
// The output fragments are inserted into RESULT.md by its coordinating author.
import fs from 'node:fs';
import path from 'node:path';

const dir = path.dirname(new URL(import.meta.url).pathname);
const read = name => fs.readFileSync(path.join(dir, name), 'utf8');
const raw = Object.fromEntries([
  'POLYNOMIAL_SETUP_ODE_ROUTE.md', 'POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md',
  'LOCAL_CONTINUATION_SETUP.md', 'LOCAL_ACTIVATION_BACKEND.md',
  'LOCAL_CONTINUATION_ASSEMBLY.md', 'LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md',
  'IMPLICIT_GAUSSIAN_SAMPLER.md', 'IMPLICIT_HARMONIC_EXECUTION.md',
  'IMPLICIT_SETUP_ORDERS.md',
].map(name => [name, read(name)]));
const cut = (s, start, end) => {
  const i = s.indexOf(start);
  if (i < 0) throw Error(`Missing start: ${start}`);
  const j = end ? s.indexOf(end, i + start.length) : s.length;
  if (j < 0) throw Error(`Missing end: ${end}`);
  return s.slice(i, j).trim();
};
const replace = (s, before, after) => {
  if (!s.includes(before)) throw Error(`Missing replacement: ${before}`);
  return s.replace(before, after);
};
const eq = (letter, n) => `[(Setup-${letter}.${n})](#eq-setup-${letter.toLowerCase()}-${n})`;
const sectionLinks = {
  'POLYNOMIAL_SETUP_ODE_ROUTE.md': ['signed defect stability', 'setup-stability'],
  'POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md': ['positive coefficient quadrature', 'setup-quadrature'],
  'LOCAL_CONTINUATION_SETUP.md': ['local Taylor continuation', 'setup-core'],
  'LOCAL_ACTIVATION_BACKEND.md': ['real-value activation backend', 'setup-activation'],
  'LOCAL_CONTINUATION_ASSEMBLY.md': ['streamed explicit assembly', 'setup-assembly'],
  'LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md': ['complete source-jet bridge', 'setup-bridge'],
  'IMPLICIT_GAUSSIAN_SAMPLER.md': ['exact adaptive Gaussian sampler', 'setup-sampler'],
  'IMPLICIT_HARMONIC_EXECUTION.md': ['implicit finite execution', 'setup-implicit'],
  'IMPLICIT_SETUP_ORDERS.md': ['deterministic order prescription', 'setup-orders'],
  'RESULT.md': ['the preceding Harmonic construction', 'harmonic-construction'],
};
const proseOnly = (s, fn) => s.split(/(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$|\$[^$\n]*\$|`[^`]*`)/g)
  .map((piece, i) => i % 2 ? piece : fn(piece)).join('');
function transform(s, letter, anchor, title) {
  const tags = [...s.matchAll(/\\tag\{([^}]+)\}/g)].map(m => m[1]);
  const tagSet = new Set(tags);
  s = proseOnly(s, text => text.replace(/\((A?\d+)\)/g, (all, label) =>
    tagSet.has(label) ? eq(letter, label.replace(/^A/, '')) : all));
  s = s.replace(/\\tag\{(A?\d+)\}/g, (_, label) => `\\tag{Setup-${letter}.${label.replace(/^A/, '')}}`);
  let ordinal = 0;
  s = s.replace(/^(#{2,3}) (.*)$/gm, (_, hashes, heading) => {
    if (hashes.length === 2) {
      ordinal += 1;
      const number = heading.match(/^(\d+)\./)?.[1] || String(ordinal);
      return `<a id="${anchor}-${number}"></a>\n##### ${heading.replace(/^\d+\. /, '')}`;
    }
    return `###### ${heading}`;
  });
  s = proseOnly(s, text => text.replace(/\bSection (\d+)\b/g,
    (_, n) => `[the ${title.toLowerCase()} subsection ${n}](#${anchor}-${n})`));
  s = s.replace(/\\\[([\s\S]*?)\\\]/g, (display, inner) => {
    const tag = inner.match(/\\tag\{Setup-([A-Z])\.(\d+)\}/);
    return tag ? `<a id="eq-setup-${tag[1].toLowerCase()}-${tag[2]}"></a>\n${display}` : display;
  });
  for (const [file, [label, target]] of Object.entries(sectionLinks)) {
    s = s.replaceAll('`' + file + '`', `[${label}](#${target})`);
    s = s.replaceAll(file, `[${label}](#${target})`);
  }
  s = proseOnly(s, text => text
    .replace(/the core\s+note/g, '[the local-continuation proof](#setup-core)')
    .replace(/the assembly\s+note/g, '[the assembly proof](#setup-assembly)')
    .replace(/the quadrature\s+note/g, '[the quadrature proof](#setup-quadrature)')
    .replace(/quadrature\s+note/g, '[quadrature proof](#setup-quadrature)')
    .replace(/the ODE route/g, '[the signed-stability proof](#setup-stability)')
    .replace(/This note/g, 'This component')
    .replace(/this note/g, 'this component')
    .replace(/frozen candidate/g, 'construction')
    .replace(/checked backend/g, 'backend')
    .replace(/already checked /g, '')
    .replace(/checked degree/g, 'certified degree')
    .replace(/checked Taylor/g, 'proved Taylor')
    .replace(/checked continuation/g, 'proved continuation')
    .replace(/checked source approximation/g, 'proved source approximation')
    .replace(/notes' local notation/g, "components' local notation")
    .replace(/For the user's comparison/g, 'For the specified Euler comparison')
    .replace(/The same note proves/g, 'The signed-stability proof above proves')
    .replace(/with the corrected/g, 'with the'));
  // A solitary TeX backslash at a source line ending is only control space.
  s = s.replace(/,\\\n/g, ',\n');
  return `<a id="${anchor}"></a>\n#### ${title}\n\n${s}\n`;
}

let stability = cut(raw['POLYNOMIAL_SETUP_ODE_ROUTE.md'], '## Deterministic setup', '## What a global coefficient solve');
let quadrature = cut(raw['POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md'], '## 1. Precise input', '**Value-oracle interface.**');
let qRates = cut(raw['POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md'], '## 7. Polylogarithmic', 'The remaining decisive gap');
qRates = replace(qRates, 'Node generation, harmonic evaluation and coefficient accumulation are\ntherefore polynomial in these logarithmic orders, with (30)--(33)\ndisplaying their dimension dependence and dense-vector factors. This\ndoes not bound \\(\\mathcal T_{\\rm val}\\) or\n\\(\\mathcal M_{\\rm val}\\). It also does not remove the dense\n\\(P\\), \\(Ln^2r\\), selection or coefficient-storage terms from\nsetup. All quadrature and dense setup arrays are discarded under the\nsame final retained-storage convention as before.',
  'Node generation and harmonic evaluation have the explicit costs (30)--(31).\nThe continuation, source projection, selection and assembly costs are proved\nbelow in [the complete source-jet bridge](#setup-bridge). All quadrature and\ndense setup arrays are discarded under the original retained-storage convention.');
quadrature += '\n\n' + qRates;
quadrature = quadrature.replaceAll('old dimension certificate', 'original dimension certificate');
// The retained spherical cutoff is ell_* throughout the integrated document.
quadrature = quadrature.replaceAll(String.raw`\mathcal Y_J`, String.raw`\mathcal Y_{\ell_*}`)
  .replaceAll(String.raw`\mathcal Y_{J}`, String.raw`\mathcal Y_{\ell_*}`)
  .replace(/\bJ\b/g, String.raw`\ell_*`)
  .replaceAll(String.raw`^\ell_*`, String.raw`^{\ell_*}`)
  .replaceAll(String.raw`_\ell_*`, String.raw`_{\ell_*}`);

let core = cut(raw['LOCAL_CONTINUATION_SETUP.md'], '## 1. Model', '## 7. Arithmetic');
core = core.replaceAll(String.raw`\mathcal Y_J`, String.raw`\mathcal Y_{\ell_*}`);
let activation = cut(raw['LOCAL_ACTIVATION_BACKEND.md'], '## 1. Domain');
activation = replace(activation, '(6)--(14) of the core note', `${eq('C',6)}--${eq('C',14)} of the core note`);
activation = replace(activation, 'product in (2)\nof the core note', `product in ${eq('C',2)}\nof the core note`);
activation = replace(activation, 'recurrence (30) of the core note', `recurrence ${eq('C',30)} of the core note`);
let assembly = cut(raw['LOCAL_CONTINUATION_ASSEMBLY.md'], '## 1. Conditional input', '## 6. Fixed-parameter');
assembly = replace(assembly, 'with its old spherical cutoff $J$ replaced by\n$\\ell_*$', 'with spherical cutoff $\\ell_*$');
assembly = replace(assembly, 'time bounds (30)--(31)', `time bounds ${eq('Q',30)}--${eq('Q',31)}`);
assembly = replace(assembly, 'Only the finite node set requires (5). A uniform local source estimate is a\nstronger sufficient input. This note does not infer (5) from mere proximity of\nthe real anchors, and does not prove their complex analytic neighborhood or\nthe convergence of the integrator. The ODE route\'s defect bound can translate a\nseparately established defect certificate into source accuracy; it is not itself\nan integrator construction.',
  'Only the finite node set requires (5). A uniform local source estimate is a\nstronger sufficient input. The local-continuation and activation proofs above\nprovide the numerical path; [the source-jet bridge](#setup-bridge) below proves\nthis stronger Euclidean source interface for its polynomial-activation jets.\nThus this conditional assembly lemma applies after that explicit interface\nreplacement, with no extra numerical-path hypothesis.');
let bridge = cut(raw['LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md'], '## 1. Precision');
bridge = replace(bridge, 'assembly equation (3)', `assembly equation ${eq('E',3)}`);
bridge = replace(bridge, 'assembly (5)', `assembly ${eq('E',5)}`);
bridge = replace(bridge, '(15)--(20) of the assembly note', `${eq('E',15)}--${eq('E',20)} of the assembly note`);
bridge = replace(bridge, 'time envelope (24) and memory envelope (25)', `time envelope ${eq('E',24)} and memory envelope ${eq('E',25)}`);
bridge = proseOnly(bridge, text => text.replace(/\(A(\d+)\)/g, (_,n) => eq('A',n)));
bridge = bridge.replaceAll("For the user's comparison", 'For the specified Euler comparison')
  .replaceAll("It meets the user's clarified Euler benchmark,", 'It provides the stated Euler comparison,');
let sampler = cut(raw['IMPLICIT_GAUSSIAN_SAMPLER.md'], '## 1. Statement');
let implicit = cut(raw['IMPLICIT_HARMONIC_EXECUTION.md'], '## 1. Inputs', '## 8. Dependencies');
implicit = replace(implicit, 'This\nsampler result is a separate proof dependency; it is not derived in this note.',
  'The [adaptive Gaussian theorem proved above](#setup-sampler) supplies this\ncontract, including its deterministic bounded-stopping and global-interleaving\nhypotheses.');
implicit = replace(implicit, 'This zero-readout convention is the one in the present study\'s `RESULT.md`.',
  'This is the zero-readout convention of the [dense model](#dense-model-and-certificates).');

const intro = String.raw`<!-- Integration provenance (scientific imports only):
Setup-S: POLYNOMIAL_SETUP_ODE_ROUTE.md, "Deterministic setup" through
  the end of the polynomial-accuracy argument; excludes global coefficient solve.
Setup-Q: POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md, sections 1--6 through
  geometry/basis costs (30)--(31), plus section 7; excludes value-oracle
  accounting and the obsolete remaining-gap paragraph.
Setup-C: LOCAL_CONTINUATION_SETUP.md, sections 1--6; generic derivative-oracle
  cost section is replaced by the real-value activation backend.
Setup-A: LOCAL_ACTIVATION_BACKEND.md, complete scientific sections.
Setup-E: LOCAL_CONTINUATION_ASSEMBLY.md, scientific sections 1--5.
Setup-B: LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md, all scientific sections.
Setup-G: IMPLICIT_GAUSSIAN_SAMPLER.md, all scientific sections.
Setup-I: IMPLICIT_HARMONIC_EXECUTION.md, scientific sections 1--7.
Orders: IMPLICIT_SETUP_ORDERS.md, scientific sections 1--9; its repeated source,
  fitting and inherited-gate recurrences are replaced by exact internal
  references and notation correspondences to the existing RESULT proofs.
No scientific input is taken from another study. Component equation tags and
prose references are namespaced; spherical cutoff J is renamed ell_* in Setup-Q.
Workflow/status metadata and unused routes are not part of these imports.
-->
<a id="harmonic-efficient-setup-proofs"></a>
<a id="efficient-setup-proofs"></a>
### Proofs of the efficient Harmonic initializers

The explicit initializer constructs source coefficients by certified local
continuation through the full source horizon. The implicit initializer executes
that same finite calculation through exact adaptive Gaussian actions. The
argument proceeds from signed defect stability and positive quadrature to
local numerical continuation, activation replacement, source assembly, and
finally the joint-law coupling and its operation count. The legacy
[initialization-jet construction](#harmonic-initial-jet-proof) remains a
separate valid alternative.

All notation referring to the dense model retains its original meaning:
\(A=W^{(1)}\), \(w=W^{(L+1)}\), \(v=x/\sqrt d\), and
\(\phi_j=\phi^{(j)}\). The parameter vector
\(\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\)
uses ordinary Euclidean/Frobenius norms and the original mean-square loss and
mobilities. This is the normalized coordinate form of the same dense flow.
The positive-label analytic branch has \(L\ge2\), \(Y>0\),
\(T\ge32(m/\gamma)\log(en)\), and
\(0<\eta\le\min(1,Y,16Ym/\gamma)\), with the full original label and
width/source qualifications. Zero labels and full-width retention keep their
separate definitions.

Each proof component scopes its auxiliary coefficient names locally. In the
quadrature component, \(a=\alpha_T/2\) is the temporal angular strip radius
and \(\ell_*\) the largest spherical degree; the continuation components use \(a\)
for the original activation strip width, and the assembly/execution components
use \(J\) for the number of time panels and \(\ell_*\) for spherical degree.
Their exact correspondence to the single order interface is given in
[the deterministic prescription](#setup-orders). In the sampler component,
\(Y,R,U,V,p,q\) are stored matrices and query-span dimensions, not network
labels, source budgets or selected widths.

The source recurrences, source event, source expansion, exact selector and
runtime comparison are proved elsewhere in this same document. Every new
deterministic and probabilistic execution argument needed for the two
initializers is included below. No source-event test or new failure allowance
is introduced. Exact joint-law equality refers to the explicit local finite
initializer with the same scalar routines and deterministic conventions; it
does not assert equality with the alternative origin-jet coefficient program.

`;
const proof = intro + [
  [stability,'S','setup-stability','Signed defect stability'],
  [quadrature,'Q','setup-quadrature','Positive coefficient quadrature'],
  [core,'C','setup-core','Local Taylor continuation from computed anchors'],
  [activation,'A','setup-activation','Real-value activation backend'],
  [assembly,'E','setup-assembly','Streamed explicit assembly'],
  [bridge,'B','setup-bridge','Source-jet compatibility and complete explicit costs'],
  [sampler,'G','setup-sampler','Exact adaptive Gaussian sampling'],
  [implicit,'I','setup-implicit','Exact implicit execution and full costs'],
].map(args => transform(...args)).join('\n');

let orders = cut(raw['IMPLICIT_SETUP_ORDERS.md'], '## 1. Inputs');
const oldSource = cut(orders, '## 2. Source constants', '## 3. Full original');
orders = replace(orders, oldSource, String.raw`## 2. Existing source constants and exact notation correspondence

Compute the source coefficients from the complete recurrences
(S.5)--(S.10), (S.22), (S.24)--(S.25), and (S.30) in
[the source foundations](#source-explicit-recurrences), in their displayed
order. Those recurrences already define every activation-only coefficient,
the source allowance \(S_*^{\rm src}\), \(K_{\rm src}\), and the actual-label
query radii \(r_t,r_q\); no source recurrence is duplicated here.

The notation correspondence is exact. Source-section
\(H_j,P_j,k_j,f_j,q_j,\tau_j\) become
\(H_j^{\rm src},P_j^{\rm src},k_j^{\rm src},f_j^{\rm src},q_j^{\rm src},\tau_j^{\rm src}\).
Write \(H_{\max}^{\rm src}=\max_jH_j^{\rm src}\),
\(k_*^{\rm src}=\max_jk_j^{\rm src}\),
\(f_*^{\rm src}=\max_jf_j^{\rm src}\), and
\(\tau_*^{\rm src}=\max_j\tau_j^{\rm src}\).
The \(V\) of (S.25) is denoted \(V_{\rm qry}\) here; \(U,T_Q,T_J,G_d\),
\(K_{\rm src},c_t,c_q,\mathcal K\) retain their source meanings.
The \(S=16Ym/\gamma\) appearing in those recurrences is the actual activity
allowance, not its upper bound one. The \(a\) in \(c_t,c_q\) is the activation
strip width. The source-budget tolerance in (S.10) is distinct from the
requested approximation error \(\eta\).
`);
const oldLabel = cut(orders, '## 3. Full original', '## 4. Width');
orders = replace(orders, oldLabel, String.raw`## 3. Full original label interval

Use the [common exact label allowance](#detailed-statements), or the
[full Harmonic allowance](#harmonic-fitting-coefficients) when only the
Harmonic theorem is needed. With \(H_D=H_d\) and \(F_D=F_d\) from
(Harmonic dense coefficients), it is
\[
0<Y\le\lambda\min\{(8H_D\sqrt{F_D})^{-1},
S_*^{\rm Leg}/8,(16H_c\sqrt{F_c})^{-1},S_*^{\rm src}/16\}.
\]
The Legendre entry is omitted for Harmonic alone. The actual activation
Gaussian moments defining \(H_D\) are those of the dense fitting theorem;
they are supplied certificates when an exact allowance is evaluated.
The setup prescription adds no label restriction and does not replace this
interval by the optional sufficient cap \(Y\le\lambda\beta^{-30L}\).
`);
const oldGates = cut(orders, '## 4. Width', '## 5. Retained');
orders = replace(orders, oldGates, String.raw`## 4. Width, confidence and inherited gates

Require \(n\ge\max(m,d)\), the explicit dense initialization threshold
\(N_{\rm fit}(\delta/32)\) from [dense fitting](#dense-fitting), and the
same source event at failure allowance at most \(\delta/32\).
The source threshold remains existential. The union bound needs no
independence; the lower-bound and central-limit events are not used here.
Retain every original radius, counting and analytic-extension gate in
[the Harmonic storage-and-gate statement](#harmonic-storage-count), including
the dimension-one gate and \(n^{-1}\le\eta_0\). These are explicit scalar
comparisons already written there. They do not test sampled matrix norms.

For use below, define the late-state displacement bound from
[the all-horizon extension](#harmonic-analytic-extension-proof),
\[
Z_n=(2Y/\sqrt\lambda+8Y\sqrt{\mathcal K}\,r_t)(en)^{-16}.
\]
The extension requires \(Z_n<b_{\rm ext}/2\), where \(b_{\rm ext}\) is
the radius denoted \(b_n\) in that earlier proof; this is distinct from the
numerical restart radius \(b_n\) defined below. Its second carrier gate is
also retained. The source amplitude and dimension coefficients used for the
exact mode count are
\[
M_{\rm amp}=10\max(H_L^{\rm src},\tau_*^{\rm src}),\qquad
b_d=2d-2,\quad D_d=2^{d+1}d^{d-2}\quad(d\ge2).
\]
No deterministic gate supplies the missing numerical confidence-to-width
threshold of the source event.
`);
orders = replace(orders, 'A deterministic sufficient selected budget is \\(q=\\min(n,9R)\\).',
  'A deterministic sufficient supplied budget is \\(Q=\\min(n,9R)\\).');
orders = replace(orders, 'If the headline convention \\(q\\ge18(2m+d+9)\\) is\ndesired, use \\(q=\\min(n,\\max\\{9R,18(2m+d+9)\\})\\).',
  'If the headline convention \\(Q\\ge18(2m+d+9)\\) is\ndesired, use \\(Q=\\min(n,\\max\\{9R,18(2m+d+9)\\})\\).');
orders = replace(orders, 'No preservation of accidental rank deficiencies is\nassumed.',
  'No preservation of accidental rank deficiencies is\nassumed. In the selected branch, the actual supports satisfy\n\\(q_j\\le9r_j\\), and the actual maximum \\(q=\\max_jq_j\\) is the\nquantity charged in the setup costs. Unused supplied budget \\(Q\\) is not padded.');
orders = proseOnly(orders, text => text.replace(/backend \(A22\)/g, `backend ${eq('A',22)}`));
orders = orders.replaceAll('The source power ledger provides', 'The [source power ledger](#source-power-ledger) provides');
orders = orders.replaceAll('the bridge\'s', '[the source-jet bridge](#setup-bridge)\'s');
orders = orders.replaceAll(String.raw`\(J,K,D,p,\ell_*,N_t,N_x,N,R,q\)`,
  String.raw`\(J,K,D,p,\ell_*,N_t,N_x,N,R,Q\)`);
const ordersIntro = String.raw`<a id="harmonic-efficient-orders"></a>
<a id="setup-orders"></a>
#### Deterministic orders for both efficient initializers

The following finite recipe supplies all orders used by the explicit and
implicit local-continuation algorithms. It reuses the exact source and fitting
coefficients already defined in this document. Every new radius, tolerance,
degree and panel count is displayed here; their error and operation arguments
are in [the complete initializer proofs](#efficient-setup-proofs).
No norm of an unknown trained path is an input. Confidence affects the
inherited admissible-width qualification, whose source portion is still not
numerically quantified.

The proof components use shorter locally scoped names. In this prescription
\(R_{\rm loc},J_{\rm loc},V_{\rm loc}\) mean their local-continuation
\(R,J,V\); \(U_j^{\rm act},K_j^{\rm act},Q_j^{\rm act},C_F^{\rm act}\)
mean the activation component's \(U_j,K_j,Q_j,C_F\); and
\(B_{\rm act},\Delta_{\rm act}\) mean its ellipse scale \(B\) and gap
\(\Delta\). Quadrature names \(a_t,h_{\rm ang},\sigma_{\rm ang},\ell_*,\mathcal Y\)
mean its \(a,h,\sigma,\ell_*,\mathcal Y_{\ell_*}\). These are exact renamings, with
no rescaling of coefficients or changes to the inequalities.

`;
const ordersOut = ordersIntro + transform(orders, 'O', 'setup-orders-detail', 'Order prescription').replace(
  '<a id="setup-orders-detail"></a>\n#### Order prescription\n\n', '');

// Emit a patch for the caller's apply_patch tool; this helper is read-only.
function compactHunks(oldText, newText) {
  const a = oldText.trimEnd().split('\n'), b = newText.trimEnd().split('\n');
  const changes = [];
  let i = 0, j = 0;
  while (i < a.length || j < b.length) {
    if (a[i] === b[j]) { i++; j++; continue; }
    const i0 = i, j0 = j;
    let match = null;
    for (let total = 1; total <= 240 && !match; total++) {
      for (let di = 0; di <= total; di++) {
        const dj = total - di;
        if (i + di >= a.length || j + dj >= b.length) continue;
        if ([0,1,2].every(k => a[i+di+k] !== undefined && a[i+di+k] === b[j+dj+k])) {
          match = [i+di,j+dj]; break;
        }
      }
    }
    [i,j] = match || [a.length,b.length];
    changes.push([i0,j0,i,j]);
  }
  const hunks = [];
  for (const [ai,bj,az,bz] of changes) {
    const h = [Math.max(0,ai-3),Math.max(0,bj-3),Math.min(a.length,az+3),Math.min(b.length,bz+3)];
    const prev = hunks.at(-1);
    if (prev && (h[0] <= prev[2] || h[1] <= prev[3])) {
      prev[2] = h[2]; prev[3] = h[3];
    } else hunks.push(h);
  }
  return hunks.map(([ai,bj,az,bz]) => '@@\n' +
    a.slice(ai,az).map(l=>'-'+l).join('\n')+'\n'+
    b.slice(bj,bz).map(l=>'+'+l).join('\n')+'\n').join('');
}
const patches = [];
for (const [name, text] of [
  ['SETUP_INTEGRATION_PROOFS.md', proof],
  ['SETUP_INTEGRATION_ORDERS.md', ordersOut],
]) {
  const target = path.join(dir, name);
  const old = fs.existsSync(target) ? fs.readFileSync(target, 'utf8') : null;
  if (old === text) continue;
  patches.push(old === null
    ? "*** Add File: " + target + "\n" + text.trimEnd().split('\n').map(l => '+' + l).join('\n') + "\n"
    : "*** Update File: " + target + "\n" + compactHunks(old, text));
}
const joined = read('RESULT.md') + '\n' + ordersOut + '\n' + proof;
const anchors = [...joined.matchAll(/<a id="([^"]+)"/g)].map(x => x[1]);
const ids = new Set(anchors);
const missing = [...new Set([...joined.matchAll(/\]\(#([^)]+)\)/g)].map(x => x[1]).filter(x => !ids.has(x)))];
const imported = ordersOut + proof;
const namespacedTags = [...imported.matchAll(/\\tag\{(Setup-[^}]+)\}/g)].map(x => x[1]);
const duplicates = namespacedTags.filter((x,i) => namespacedTags.indexOf(x) !== i);
console.log(JSON.stringify({patch:'*** Begin Patch\n'+patches.join('')+'*** End Patch\n', report:{proofLines:proof.split('\n').length,orderLines:ordersOut.split('\n').length,namespacedTags:namespacedTags.length,duplicates,missingAnchors:missing}}));
