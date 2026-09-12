"""Assemble the proposed C.4.9 text from frozen study proof components.

This edits only study-owned proposal files. It never edits established docs.
"""
from pathlib import Path
import hashlib, json, re
ROOT=Path(__file__).resolve().parent

def section(name,start,end=None):
    s=(ROOT/name).read_text()
    a=s.index(start)
    b=s.index(end,a) if end else len(s)
    return s[a:b].strip()

def headings(s,unit):
    s=re.sub(r'^## (\d+)\. (.+)$',lambda m:'###### '+unit+'.'+m[1]+'. '+m[2],s,flags=re.M)
    s=re.sub(r'^### (.+)$',lambda m:'**'+m[1]+'**',s,flags=re.M)
    return s

main=(ROOT/'CANONICAL_STATEMENT_DRAFT.md').read_text().strip()
main += '\n\nEquation labels and auxiliary constants are local to each proof unit below.\nAll finite vector norms are ordinary Euclidean norms; normalization factors\nare displayed in the finite-state metric.\n'
a=section('CONTINUATION_CONTROL_TUBE.md','## 1. Statement','## 7. Strong completion')
a=a[:a.index('The raw Euler approximations converge strongly')]+'''The assertion here is a finite-program source bound. Proof unit C constructs
the required strong nonlinear trajectories from these bounds; proof unit D
identifies actual finite GF. No probability supremum over random finite-network
feedback controls is asserted by this source estimate.

'''+a[a.index('## 2. Why control time'):]
a=headings(a,'A')
a=a.replace('This completes the controlled source-tube theorem.','This proves the signed-control source theorem used below.')
a=a.replace('Those feedback passages require the application described in section 8.','Endogenous mixture feedback is treated in proof unit C and actual finite GF in proof unit D.')
a=a.replace('section 8','proof unit C')
a=a.replace('Set \\(L=L_*+1\\) and restrict \\(q\\le1\\).','Set \\(M_0=\\|A_0\\|\\le2\\), \\(L=L_*+1\\), and restrict \\(q\\le1\\).')
# Distinguish a comparison difference from the typed upper backward field.
a=a.replace('\\Delta^2','\\Delta^{(2)}')
a=a.replace('\\Delta\\Delta^{(2)}','\\mathrm d\\Delta^{(2)}')
for token in ['D','F','C','U','V','H','Z','Q']:
    a=a.replace('\\Delta '+token,'\\mathrm d '+token)
a=a.replace('\\Delta\\phi','\\mathrm d\\phi').replace('(\\Delta F','(\\mathrm d F')
a+='\n\nHere \\(\\mathrm d X=X-\\bar X\\) denotes a comparison difference;\n\\(\\Delta^{(2)}\\) is the typed upper backward field.\n'
app=section('CONTROL_TUBE_APPLICATION_NOTES.md','## 4. Named-coefficient continuity','## 5. Check')
app=headings(app,'A-supplement')
app=app.replace('The reference anchor CT21–CT25','The reference anchor (CT21)–(CT25)')
app=app.replace('I find no omitted named-coefficient continuity dependency in\nthis reconstruction. The canonical proof packet should retain\nthe complete contained III.F source/regularization proof and\nC.4.5.2\'s clipping/forcing proof, since naming their theorems\nwithout these bodies would conceal precisely the delicate step.\nNo all-orders jet theorem or uniform derivative convergence of\nfinite GF is needed for this anchor.','The contained III.F source/regularization proof and C.4.5.2 clipping/forcing\nargument supply these fixed-graph constructions. No all-orders jet theorem\nor uniform derivative convergence of finite GF is needed for this anchor.')
# Full geometry and activity proof; its common existence premise is proved next.
b=section('CONDITIONING_ACTIVITY.md','## 2. Endpoint conditioning','## 6. What common-primitive')
b=headings(b,'B')
for old,new in [('(1.1)','(NS1)'),('(1.3)','(NS3)'),('(1.4)','the anchor assertion'),('(1.5)','(NS6)'),('(1.6)','(NS7)')]: b=b.replace(old,new)
b=b.replace('the source-regular flow premise','the constructed source-regular flow')
b=b.replace('d=||theta-theta_dagger||_H','d=||theta-theta_dagger||_raw')
b=b.replace("the present note supplies no singular-limit identification.","Its original-mixture identification is proved in proof unit C.")
b='For the activity implication in this unit, let \\(\\tau_{ex}>0\\) be a common\nexistence interval for (NS3); proof unit C constructs it. The endpoint\nconditioning and continuity estimates do not assume that existence.\n\n'+b
c=section('SLOW_SELECTION.md','## 2. Consequences','## 8. Actual finite')
c=r'''## 1. State and source interface

Use the state and initialized carrier in (NS2), and write its raw increment
space as \(\mathcal E\). Throughout this unit inputs in \(f_\theta(u)\)
are normalized; the reconstructed physical prediction is evaluated at
\(x=\sqrt2u\). For clarity the fields used in the comparisons are
\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),
 \quad f_\theta(u)=\langle c,H^2(u)\rangle,
\]
\[
 \Delta(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta(u),\quad
 g_u=(\phi'(w\cdot u)Q(u)u,\Delta(u)\otimes H^1(u),H^2(u)).\tag{1}
\]
The scalar prediction is continuously differentiable in the raw metric by
the contained scalar-gradient argument in A.4. Set
\[
 p=(\alpha,y)\in\mathcal P=I\times[3/8,5/8],\qquad
 I=[\pi/4-1/1216,\pi/4+1/1216].\tag{2}
\]
All constants below are uniform in this compact box. The reference feature
curve is exactly
\[
 \theta_s=\tfrac12g_{e_1}(\theta)-\tfrac12g_{e_2}(\theta),\tag{3}
\]
and C.4.5 proves the raw endpoint and residual bounds
\[
 \|\theta_*(t)-\theta_\dagger\|_{\rm raw}\le\sqrt{10}e^{-t/5},
 \qquad |r_*(t)|\le\sqrt2 e^{-t/5}.\tag{4}
\]
Its physical control is \(a_*=(e_*,-e_*,0)\), with total absolute mass
\(s_\dagger\le10\). For the three inputs \(e_1,e_2,u_\alpha\), raw Euler is
\[
 \theta_{k+1}=\theta_k+\sum_{j=1}^3\gamma_{kj}g_{u_j}(\theta_k).\tag{5}
\]
Let SCT denote the source estimate of proof unit A: there are uniform
\(\delta_{\rm src},h_{\rm src}>0\) and \(B_{\rm src}<\infty\) for all
such finite histories satisfying
\[
 \int|a(t)-a_*(t)|_1dt<\delta_{\rm src}.\tag{6}
\]
The mesh is measured by \((|a|_1+|a_*|_1)dt\). Every passive backward row,
including its distinguished current source and all old training sources,
then has the stated cap. Deterministic feedback coefficients are frozen
under named differentiation, just as in (CT12)–(CT16).

The physical reference keeps running after every finite prefix. A prefix
through \(b\) followed by appended controls has distance at most the
appended absolute mass plus \(s_\dagger-s_*(b)\), including a zero extension
after the episode. This supplies the endpoint interface without a source
reset. All subsequent constructions use this exact full-history condition.

'''+c
c=c.replace("This is the conditioning route's Lemma 4.1; the needed two-input\nargument is short enough to record.","This follows from proof unit B.")
start=c.index('C.4.6.S43--44 give a common subGaussian envelope')
stop=c.index('By joint raw gradient continuity',start)
c=c[:start]+c[stop:]
c=headings(c,'C')
c=c.replace('I=[\\pi/4-a,\\pi/4+a],\\quad 0<a<\\pi/8,','I=[\\pi/4-a,\\pi/4+a],\\quad a=1/1216,')
c=c.replace('The coordinator may decrease \\(a>0\\) to obtain its learning margins. Every','Every')
c=c.replace("the conditioning route's Lemma 4.1","proof unit B's endpoint conditioning")
c=c.replace('the frozen controlled source theorem','the signed-control source theorem in proof unit A')
c=c.replace('the frozen continuation module','proof unit A')
c=c.replace('frozen continuation module','source theorem of proof unit A')
c=c.replace("the coordinator's paired hidden-activation margin","the paired hidden-activation margin in proof unit B")
c=c.replace("coordinator's paired hidden-activation margin","paired hidden-activation margin in proof unit B")
c=c.replace('CONTINUATION_CONTROL_TUBE.md','proof unit A')
c=c.replace('\\Delta','\\Delta^{(2)}')
# The finite proof is a proved implication, whose premises C has just verified.
d=section('FINITE_CAPTURE.md','## Statement needed','## Quantifiers')
d=d.replace('## Statement needed from the population construction','###### D.1. Fixed-horizon population-to-finite bridge')
d=d.replace('## Proof','###### D.2. Proof')
d=d.replace('The new population selection theorem (when proved)','The population selection theorem of proof unit C')
d=d.replace('the new population selection theorem (when proved)','the population selection theorem of proof unit C')
d=d.replace('new population selection theorem (when proved)','population selection theorem of proof unit C')
d=d.replace('At width n give each layer\'s vector space its normalized Euclidean inner\nproduct n^{-1}sum. Middle increments have ordinary Frobenius norm. The raw\nstate-increment metric is\n\n    d_n^2=||w-wbar||_(n,2)^2+||W2-W2bar||_F^2\n                                      +||c-cbar||_(n,2)^2.','At width n all vector and matrix norms are ordinary Euclidean, Frobenius or\noperator norms. The raw state-increment metric is\n\n    d_n^2=||W1-W1bar||_F^2/n+||W2-W2bar||_F^2+||c-cbar||_2^2/n.')
end=r'''##### Completion of the theorem

Take the common constrained existence time from proof unit C as the
\\(\\tau_{ex}\\) used in proof unit B, and use B's smaller positive time as
our final \\(\\tau_0\\). Decreasing a time already constructed preserves every
source bound, uniqueness statement and mixture continuation estimate. Set
\\(a=\\eta_R\\) from (5.5) and \\(j=\\eta_H\\) from (5.7), both in proof unit B.
They depend only on the fixed reference and parameter rectangle.

Proof unit C proves (NS5) uniformly over that rectangle, in the original
unshifted physical times \\(t=\\tau/\\epsilon\\). Its original-mixture Euler
programs verify all the population hypotheses of proof unit D for each fixed
positive \\(\\epsilon\\). Thus D proves (NS8) and the joint same-array
observation contract. At \\(T_\\epsilon\\), the population reference tends
strongly to \\(\\theta_\\dagger\\). The forward field inequalities therefore
identify (NS9)'s limit with (NS7), using paired programs on the same initialized
arrays, followed only then by \\(\\epsilon\\downarrow0\\).

On the common bounded prediction region, squared loss at the one added atom
is continuous. Hence the probability that
\\(R_{\\nu}(F_*)-R_{\\nu}(f_{n,\\mu_\\epsilon}(T_\\epsilon))\\ge a/2\\)
and \\(J_{2,n,\\epsilon}\\ge j/2\\) tends to one in the displayed iterated order.
This verifies every assertion of the theorem. The state reconstruction retains
the evolving hidden features and actual adjoint throughout the episode.
'''.replace('\\\\','\\')
text=main+'\n\n##### Proof unit A. Uniform source control in accumulated training force\n\n'+a+'\n\n'+app+'\n\n##### Proof unit B. Endpoint conditioning and finite nonlinear learning\n\n'+b+'\n\n##### Proof unit C. Original-initialization continuation and slow selection\n\n'+c+'\n\n##### Proof unit D. Actual finite gradient flow and paired observations\n\n'+d+'\n\n'+end
(ROOT/'CANONICAL_ADDITION_v1.md').write_text(text+'\n')
inputs=['CANONICAL_STATEMENT_DRAFT.md','CONTINUATION_CONTROL_TUBE.md','CONTROL_TUBE_APPLICATION_NOTES.md','CONDITIONING_ACTIVITY.md','SLOW_SELECTION.md','FINITE_CAPTURE.md']
manifest={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in inputs}
manifest['CANONICAL_ADDITION_v1.md']=hashlib.sha256((ROOT/'CANONICAL_ADDITION_v1.md').read_bytes()).hexdigest()
(ROOT/'ASSEMBLY_MANIFEST_v1.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(len(text.splitlines()),manifest['CANONICAL_ADDITION_v1.md'])
