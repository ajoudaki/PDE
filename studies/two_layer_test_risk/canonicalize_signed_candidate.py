"""Canonical notation-only assembly of the frozen signed C.4 candidate.

This never calls a coefficient producer or writes the established book. It
requires the exact original candidate, retains an invertible edit map, and
checks every displayed formula after independently undoing notation changes.
Run from any directory; --output must name a fresh study-generated directory.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / "PROMOTION_SIGN_C4.md"
TARGET = HERE / "PROMOTION_SIGN_C4_V2.md"
SOURCE_SHA256 = "ae5eff6e5c351410355048f56f8b429383612cbf30558178069e0f8692b2025f"
BUILDER_SHA256 = "af0b4089124aafcd8006b7b9372fc0a4a338fa4ef2f4b66fe3a08ec4ec0c6dce"
SECTION_MARKER = "#### C.4 certificate: "


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


class Editor:
    def __init__(self, text: str, section: str):
        self.text, self.section, self.edits = text, section, []

    def sub(self, old: str, new: str, reason: str, count: int | None = 1):
        actual = self.text.count(old)
        if actual == 0 or (count is not None and actual != count):
            raise ValueError((self.section, reason, actual, count, old))
        # Locations refer to the section immediately before this operation.
        positions = [m.start() for m in re.finditer(re.escape(old), self.text)]
        self.edits.append(dict(section=self.section, reason=reason,
                               old=old, new=new, count=actual,
                               before_offsets=positions))
        self.text = self.text.replace(old, new)

    def pattern(self, pattern: str, replacement, reason: str):
        matches = list(re.finditer(pattern, self.text))
        if not matches:
            raise ValueError((self.section, reason, pattern))
        for match in reversed(matches):
            old = match.group()
            new = replacement(match)
            self.edits.append(dict(section=self.section, reason=reason,
                                   old=old, new=new, count=1,
                                   before_offsets=[match.start()]))
            self.text = self.text[:match.start()] + new + self.text[match.end():]


def in_math(text: str, transform) -> str:
    """Change inline/display mathematics, keeping protocol fences verbatim."""
    parts = re.split(r"(```.*?```|`[^`\n]+`|\\\[.*?\\\])", text, flags=re.S)
    for i, part in enumerate(parts):
        if part.startswith("```"):
            continue
        if part.startswith("`"):
            parts[i] = "`" + transform(part[1:-1], False) + "`"
        elif part.startswith(r"\["):
            parts[i] = r"\[" + transform(part[2:-2], True) + r"\]"
    return "".join(parts)


def fields(text: str, display: bool, *, upper_alias: str = "d",
           lower: bool = False, scalar: bool = False) -> str:
    """Expand only mathematical aliases; never alter JSON/protocol names."""
    phi = r"\phi" if display else "phi"
    sup = lambda layer: "^{(" + str(layer) + ")}" if display else "^(" + str(layer) + ")"
    if upper_alias == "D":
        text = re.sub(r"E_([abijx])", lambda m: phi + "''(Y_" + m[1] + ")", text)
        text = re.sub(r"D_([abijx])", lambda m: phi + "'(Y_" + m[1] + ")", text)
    else:
        text = re.sub(r"(?:dd|d')_([abijx])", lambda m: phi + "''(Y_" + m[1] + ")", text)
        text = re.sub(r"d_([abijx])", lambda m: phi + "'(Y_" + m[1] + ")", text)
    if lower:
        text = re.sub(r"e_([abijx])", lambda m: phi + "'(Z_" + m[1] + ")", text)
        text = re.sub(r"h_([abijx])", lambda m: "H_" + m[1] + sup(1), text)
    # Match only the old bare upper field, not a newly inserted lower field.
    text = re.sub(r"H_([abijx])(?!lpha|\^)", lambda m: "H_" + m[1] + sup(2), text)
    if scalar:
        text = re.sub(r"\bH(?=\(|'|\||`|$)", lambda _: phi, text)
        text = text.replace("D(z)", phi + "'(z)").replace("E(z)", phi + "''(z)")
    return text


def typed_moments(text: str, display: bool) -> str:
    """Type expectations according to the coordinate functions inside them."""
    def bracket(m):
        body = m[1]
        is_lower = ("Z_" in body or "^(1)" in body or "^{(1)}" in body)
        return ("E_1[" if is_lower else "E_2[") + body + "]"
    text = re.sub(r"E\[([^\[\]]*)\]", bracket, text)
    text = re.sub(r"(?<![\w])E (?=[SH]|phi|\\partial|\\phi)", "E_2 ", text)
    return text


def edit_math(e: Editor, function, reason: str):
    # Store exact changed math fragments separately, not whole sections.
    pattern = r"```.*?```|`[^`\n]+`|\\\[.*?\\\]"
    matches = list(re.finditer(pattern, e.text, re.S))
    for match in reversed(matches):
        old = match.group()
        if old.startswith("```"):
            continue
        new = in_math(old, function)
        if old != new:
            e.edits.append(dict(section=e.section, reason=reason, old=old,
                                new=new, count=1, before_offsets=[match.start()]))
            e.text = e.text[:match.start()] + new + e.text[match.end():]


def assemble(original: str):
    raw = original.split(SECTION_MARKER)
    names = ["primary C4"] + [v.splitlines()[0] for v in raw[1:]]
    editors = [Editor(t, n) for t, n in zip(raw, names)]
    base, err, eng, ang, drv, conclusion = editors
    base.sub(r"E[\Gamma_{F_1}\Gamma_{F_2}]", r"E_1[\Gamma_{F_1}\Gamma_{F_2}]",
             "Type the lower-population innovation covariance in C4.31")
    base.sub("L(g_tau(t))=L(f_t)", "L_g(tau(t))=L_f(t)",
             "Use the defined trained and frozen loss functions")
    base.sub("is established here.\n", "is established here.\n\n",
             "Separate the proof from the certificate heading")

    err.sub("All expectations are normalized Gaussian expectations.",
            "All Gaussian expectations are normalized. The symbols `E_1` and `E_2`\n"
            "retain their population meanings from (C4.4); generic Gaussian laws\n"
            "are specified explicitly. The integer `q` in the cubature lemma counts\n"
            "Gaussian root coordinates and is unrelated to the network input dimension.",
            "Distinguish generic Gaussian integrals and the two populations")
    for old, new in [("F:R^d", "F:R^q"), ("N_d", "N_q"), ("Q_d", "Q_q"),
                     ("j=1}^d", "j=1}^q"), ("I_d", "I_q"),
                     ("dimensions `d<=4`", "root dimensions `q<=4`")]:
        err.sub(old, new, "Use q for generic cubature dimension", None)
    err.sub("For positive `h_j`,", "Let `N_1,...,N_q` be independent standard normal variables.\nFor positive `h_j`,",
            "Specify the generic root law")
    err.sub("E F(N_1,", "E_{N(0,I_q)} F(N_1,", "Label generic Gaussian expectation")
    err.sub("Put `H(z)=tanh z`, `D(z)=H'(z)`, `E(z)=H''(z)`. For `|Im z|<=pi/4`,",
            "For `phi(z)=tanh z` and `|Im z|<=pi/4`,", "Remove scalar derivative aliases")
    err.sub("`E=-2HD`", "`phi''=-2phi phi'`", "Expand scalar derivative identity")
    err.sub("factors `D` and `s` factors `E`", "factors `phi'` and `s` factors `phi''`",
            "Expand derivative factor names")
    err.sub("number of factors `H`", "number of factors `phi`", "Use canonical activation name")
    err.sub("For example, with `P=sum_a|p_a|=(1+sqrt(5))/6<.54`,",
            "Throughout the certificate set `P=27/50`, so\n"
            "`sum_a|p_a|=(1+sqrt(5))/6<P`. Then, for example,",
            "Use the same rational label bound throughout the certificate")
    err.sub("`Q`, `L`, and `T`", "`Q`, `L`, and `mathcal T` from (C4.27)",
            "Map lower fourth-order tensor to C4.27")
    err.sub("A concrete parameter choice available before a numerical result is to fix\n`R=8`",
            "For a concrete parameter choice, fix the root radius at eight",
            "Remove process chronology and avoid overloading risk R")
    err.sub("for `H`, `(1,2)` for `D`, and `(2,5)`\nfor `E`",
            "for `phi`, `(1,2)` for `phi'`, and `(2,5)`\nfor `phi''`",
            "Expand Hessian factor names")
    edit_math(err, lambda s, d: fields(s, d, upper_alias="D", scalar=True),
              "Expand scalar and indexed activation aliases")
    edit_math(err, typed_moments, "Type upper moment expectations")
    err.sub("Here `delta E` denotes the difference between the two covariance laws,\nnot a derivative in time.",
            "Here `delta E_2[F]=E_{N(0,Q)}[F]-E_{N(0,Qbar)}[F]` denotes\n"
            "the difference of the upper-coordinate integrals under the two specified\n"
            "covariance laws; it is not a derivative in time.",
            "Define covariance perturbation without changing population meaning")
    err.sub("in the original derivation.", "in (C4.27)--(C4.30).", "Replace historical reference")
    err.sub("`n` consecutive binary operations have unit roundoff `u` and `nu<1`",
            "`k` consecutive binary operations have unit roundoff `u` and `ku<1`",
            "Distinguish arithmetic operation count from network width")
    err.sub("`gamma_n=nu/(1-nu)`", "`gamma_k=ku/(1-ku)`", "Rename arithmetic operation count")
    err.sub("This\nsentence specifies a construction, not a claimed error constant for an\nuninspected implementation. The same construction handles Gaussian\nweights after suitable range reduction.",
            "The implementation and its operation-by-operation error constants\n"
            "are given below. The same construction handles Gaussian weights after\n"
            "suitable range reduction.", "Replace stale implementation-status language")

    first = eng.text.index("Training slots are")
    last = eng.text.index("##### Finite-rule implementation")
    eng.sub(eng.text[first:last],
        "The mathematical slots remain `I={x,1,2,3}`, with training indices\n"
        "`1,2,3` and `p_x=0`. The C++ array index bijection is\n"
        "`iota(1)=0`, `iota(2)=1`, `iota(3)=2`, and `iota(x)=3`.\n"
        "Thus the mathematical label `p_a` is the token `p0`, `p1`, or `p2`\n"
        "when `a=1`, `2`, or `3`, respectively. Every slot of each code array\n"
        "uses this bijection, including all four slots of `T_bits`.\n\n"
        "Use `H_i^(2)=phi(Y_i)` and `S=sum_(a=1)^3 p_a H_a^(2)`. Take a\n"
        "specified real factor `Lhat` whose training rows have zero fourth column,\n"
        "and set `Y_i=sum_(j=1)^4 Lhat_(iota(i),j-1) gamma_j`, with independent\n"
        "standard normal roots `gamma_1,...,gamma_4`. Here `E_gamma` means their\n"
        "joint expectation. For covariance Q these coordinate integrals equal\n"
        "the population expectations `E_2`. The executing rule uses an exact\n"
        "dyadic factor and charges its covariance discrepancy by (C4.E6);\n"
        "the following conditioning identities hold for either specified factor.\n\n"
        "Conditional on `gamma_1,gamma_2,gamma_3`, all training quantities are\n"
        "fixed and `Y_x=m_x+sigma_x gamma_4`, where\n"
        "`m_x=sum_(j=1)^3 Lhat_(3,j-1) gamma_j` and `sigma_x=Lhat_(3,3)`.\n"
        "For a scalar function v, define the conditional root integral\n"
        "`E_{gamma_4}[v(Y_x)]=integral_R v(m_x+sigma_x z) exp(-z^2/2) dz/sqrt(2pi)`.\n"
        "This integrates the fourth independent root, not a hidden population.\n"
        "The three scalar functions of the retained roots are\n\n"
        "`A=E_{gamma_4}[phi(Y_x)]`, `B=E_{gamma_4}[phi'(Y_x)]`,\n"
        "and `C=E_{gamma_4}[phi''(Y_x)]`.\n\n"
        "Write `E_{gamma_1:3}` for expectation over the first three independent\n"
        "standard normal roots. The seventeen distinct dynamic outer moments are\n\n"
        "- `E_{gamma_1:3}[S^2 B phi'(Y_b)]`, three values (`dynamic_V`);\n"
        "- `E_{gamma_1:3}[S A phi'(Y_a)phi'(Y_b)]`, six symmetric values (`dynamic_C`);\n"
        "- `E_{gamma_1:3}[B phi'(Y_a)]`, three values (`dynamic_dd`);\n"
        "- `E_{gamma_1:3}[S C]`, one value (`dynamic_ESdd`);\n"
        "- `E_{gamma_1:3}[A phi''(Y_a)]`, three values (`dynamic_Hdd`);\n"
        "- `E_{gamma_1:3}[S A]`, one value (`dynamic_SH`).\n\n"
        "These are conditional forms of the full root integrals. At covariance Q,\n"
        "for example, `V_xb=E_2[S^2 phi'(Y_x)phi'(Y_b)]`, and `dynamic_C`\n"
        "represents `E_2[H_x^(2) S phi'(Y_a)phi'(Y_b)]`. The two\n"
        "reverse-response derivatives in (C4.30) are\n\n"
        "`E_2[partial_i U_x]=p_i E_2[phi'(Y_i)phi'(Y_x)]+1_(i=x) E_2[S phi''(Y_x)]`,\n\n"
        "`E_2[partial_i(H_x^(2)phi'(Y_a))]=1_(i=x) E_2[phi'(Y_x)phi'(Y_a)]+1_(i=a) E_2[H_x^(2)phi''(Y_a)]`.\n\n"
        "For a dyadic factor the same identities use its specified `E_gamma` law.\n"
        "Both matrix responses are retained. The training moments corresponding to\n"
        "`E_2[S^2]`, `E_2[S^2 phi'(Y_a)phi'(Y_b)]`,\n"
        "`E_2[phi'(Y_a)phi'(Y_b)]`, and `E_2[S phi''(Y_a)]` use only the\n"
        "first three roots. Lower moments are the two-root tensors `Q_ij`,\n"
        "`L_ab`, and `mathcal T_abij` of (C4.27), with their expectation `E_1`.\n"
        "Expanding `S^2 phi'(Y_x)phi'(Y_b)` includes terms with four distinct\n"
        "upper coordinates. Conditioning preserves that full law.\n\n",
        "Specify the index bijection and conditional root integrals; preserve all moment formulas")
    eng.sub("16,16,256 entries, and the last tensor is ordered `(a,b,i,j)`.",
            "16,16,256 entries. They approximate the corresponding `Q`, `L`, and\n"
            "`mathcal T` moments under the supplied dyadic lower law. The last tensor\n"
            "is ordered `(iota(a),iota(b),iota(i),iota(j))`; its flat offset is\n"
            "`64 iota(a)+16 iota(b)+4 iota(i)+iota(j)`. The name `T_bits` is a\n"
            "code key for the tensor `mathcal T` in (C4.27), not the field `T_x`.",
            "Specify lower-array tensor layout and canonical tensor identity")
    eng.sub("of `d=1-H^2`, `dd=-2H+2H^3` on `[-1,1]` gives errors at most `1.3e-11` and",
            "of `phi'(z)=1-phi(z)^2`, `phi''(z)=-2phi(z)+2phi(z)^3` for\n"
            "`phi(z) in[-1,1]` gives errors at most `1.3e-11` and",
            "Expand arithmetic derivative formulas")
    eng.sub("For completeness, the real integrands contain only `H,d,dd,S` with\n`|H|,|d|<=1`, `|dd|<=2`, `|S|<=1`; `S` is a three-term weighted sum.",
            "For completeness, the real integrands contain only activation values,\n"
            "their first two derivatives, and S. On real arguments,\n"
            "`|phi|,|phi'|,|phi''|<=1` by (C4.E7), and `|S|<=1`; S is a\n"
            "three-term weighted sum.\n"
            "The code-local arrays `H`, `d`, `dd` evaluate `H_i^(2)`, `phi'(Y_i)`,\n"
            "`phi''(Y_i)`; the lower arrays `h`, `e` evaluate `H_i^(1)`, `phi'(Z_i)`.",
            "State canonical factors while retaining code-local names explicitly")

    ang.sub("`h_alpha=phi(Z_alpha)`", "`H_alpha^(1)=phi(Z_alpha)`", "Type lower angular field")
    ang.sub("`|beta|<=1/10`. Put `P=sum_a |p_a|=(1+sqrt(5))/6<27/50` and",
            "`|beta|<=1/10`. Use `P=27/50` and `sum_a|p_a|<P` as above.\n"
            "Write `J(alpha)=J(x(alpha))`, `a(alpha)=a(x(alpha))`, and",
            "Keep the label bound fixed and define angular evaluation shorthand")
    ang.sub("`E[h_alpha h_theta]`", "`E_1[H_alpha^(1) H_theta^(1)]`", "Type angular covariance")
    ang.sub("`h_alpha`", "`H_alpha^(1)`", "Type lower process span")
    ang.sub("`||h_alpha^(k)||_2`", "`||partial_alpha^k H_alpha^(1)||_2`", "Separate layer and derivative orders")
    ang.sub("`s_k>=||h_alpha^(k)||_2`", "`s_k>=||partial_alpha^k H_alpha^(1)||_2`", "Separate layer and derivative orders")
    ang.sub("Let `mu_j` be the following rational upper bound for `E|N|^j`:",
            "For a scalar `N~N(0,1)`, let `mu_j` be the following rational upper\n"
            "bound for `E_{N(0,1)}|N|^j`:", "Specify scalar normal moment law")
    ang.sub("sqrt(E|N|^(2j))", "sqrt(E_{N(0,1)}|N|^(2j))", "Type scalar Gaussian moment")
    ang.sub("Use lower `h_i=phi(Z_i), e_i=phi'(Z_i)` and upper\n`H_i=phi(Y_i), d_i=phi'(Y_i), d'_i=phi''(Y_i)`.",
            "Use the lower fields `H_i^(1)=phi(Z_i)` and upper fields\n"
            "`H_i^(2)=phi(Y_i)` from (C4.4), with activation derivatives written\n"
            "explicitly. Each `E_1` or `E_2` below contracts only its own population.",
            "Use canonical population fields in angular proof")
    edit_math(ang, lambda s, d: typed_moments(fields(s, d, lower=True), d),
              "Canonicalize angular coefficient factors and population contractions")
    edit_math(ang, lambda s, d: scalar_contributions(s, d),
              "Distinguish scalar angular contributions from initialized fields")
    ang.sub("`J=4mathcal F(alpha)+(4/3)mathcal B(alpha)`",
            "`J(alpha)=4mathcal F(alpha)+(4/3)mathcal B(alpha)`",
            "Use the defined angular evaluation of J")
    ang.sub("where\n\n", "where `x=x(alpha)` and\n\n", "Specify the passive angular input", 1)
    ang.sub("Finally, reflection of both initial roots and the symmetric training\nlabels gives",
            "Finally, the lower-root reflection `(xi_1,xi_2)->(xi_1,-xi_2)`,\n"
            "together with exchange of training indices 2 and 3 and their equal\n"
            "labels, gives", "Specify the reflection already used by the symmetry proof")

    drv.sub("`T_abij=E[e_a e_b h_i h_j]`", "`mathcal T_abij=E[e_a e_b h_i h_j]`",
            "Use C4.27 tensor in lower table")
    drv.sub("T_{abij}", r"\mathcal T_{abij}", "Use C4.27 tensor in exact contraction")
    drv.sub("With `H_i=tanh(Y_i), d_i=tanh'(Y_i), dd_i=tanh''(Y_i)` and\n`S=sum p_a H_a`,",
            "With `H_i^(2)=phi(Y_i)`, `phi=tanh`, and\n`S=sum p_a H_a^(2)`,",
            "Remove upper derivative aliases in interval assembly")
    drv.sub("The interval assembly uses training-only indices a,b,i,j and passive x=3.\nDefine",
            "The interval assembly uses mathematical training indices `a,b,i,j` in\n"
            "`{1,2,3}` and the passive slot x. Its arrays use the bijection iota\n"
            "specified above. Define", "Preserve mathematical slots across interval assembly")
    edit_math(drv, lambda s, d: typed_moments(fields(s, d, lower=("E[h" in s or "E[e" in s)), d),
              "Canonicalize interval-assembly factors and population contractions")
    edit_math(drv, lambda s, d: scalar_contributions(s, d),
              "Use the defined scalar angular contributions in interval assembly")
    drv.sub("response terms enter F", "response terms enter `mathcal F(alpha)`",
            "Name the scalar forward contribution")
    drv.sub("response terms enter B", "response terms enter `mathcal B(alpha)`",
            "Name the scalar readout contribution")
    drv.sub("`J_x=4mathcal F(alpha)+(4/3)mathcal B(alpha)`",
            "`J(alpha)=4mathcal F(alpha)+(4/3)mathcal B(alpha)`",
            "Use the defined angular evaluation of J")
    drv.sub("`a_x=2 E_2[S H_x^(2)]`", "`a(alpha)=2 E_2[S H_x^(2)]`",
            "Use the defined angular evaluation of a")
    drv.sub("The exact symmetry-reduced periodic mean is enclosed by the interval sum",
            "Write `J_j=J(2pi j/256)` and `a_j=a(2pi j/256)` for angular\n"
            "node values. The exact symmetry-reduced periodic mean is enclosed by\n"
            "the interval sum", "Distinguish angular nodes from training indices")
    drv.sub("level enters this decision. The final claim remains conditional on inspection\nof the full mathematical and executing source, rather than trusting a flag.",
            "level enters this decision. The sign proof combines the full mathematical\n"
            "error bounds with the executing source and its checked arithmetic contracts.",
            "Replace stale review-condition language with actual proof dependencies")
    drv.sub("Delta(t)", "R(g_tau(t))-R(f_t)", "Spell out the matched-risk observable", 2)

    for e in editors[1:]:
        # Rewrap only overlong prose lines; never equations, tables, lists,
        # protocol blocks, or complete inline formulas.
        displayed = fenced = False
        for line in e.text.splitlines():
            if line.strip() == r"\[":
                displayed = True
            if line.startswith("```"):
                fenced = not fenced
            if not displayed and not fenced and re.match(r"[A-Za-z]", line) and len(line) > 100:
                tokens = re.findall(r"`[^`]*`[.,;:!?]?|\S+", line)
                lines, current = [], ""
                for token in tokens:
                    if current and len(current) + len(token) + 1 > 80:
                        lines.append(current)
                        current = token
                    else:
                        current += (" " if current else "") + token
                if current:
                    lines.append(current)
                wrapped = "\n".join(lines)
                if wrapped != line:
                    e.sub(line, wrapped, "Rewrap prose without changing its tokens")
            if line.strip() == r"\]":
                displayed = False
    result = SECTION_MARKER.join(e.text for e in editors)
    return result, editors


def scalar_contributions(text: str, display: bool) -> str:
    prefix = r"\mathcal " if display else "mathcal "
    arg = r"\alpha" if display else "alpha"
    for name in ("F", "B"):
        text = text.replace(name + "_x^{(k)}", prefix + name + "^{(k)}(" + arg + ")")
        text = text.replace(name + "_x", prefix + name + "(" + arg + ")")
    text = text.replace("a_x^{(k)}", "a^{(k)}(" + arg + ")")
    return text


def display_canonical(text: str, section: str) -> str:
    """Independent inverse notation normalization for formula comparison."""
    text = re.sub(r"E_[12](?=[\[ ])", "E", text)
    if section == "Gaussian integration and covariance":
        text = text.replace("E_{N(0,I_q)}", "E")
        for old, new in [("N_q", "N_d"), ("Q_q", "Q_d"), ("j=1}^q", "j=1}^d")]:
            text = text.replace(old, new)
        text = re.sub(r"\\phi''\(Y_([abijx])\)", r"E_\1", text)
        text = re.sub(r"\\phi'\(Y_([abijx])\)", r"D_\1", text)
        text = text.replace(r"\phi''(z)", "E(z)").replace(r"\phi'(z)", "D(z)")
        text = text.replace(r"\phi", "H")
    elif section in ("the circle rule", "exact interval assembly"):
        for name in ("F", "B"):
            text = text.replace(r"\mathcal " + name + r"^{(k)}(\alpha)", name + "_x^{(k)}")
            text = text.replace(r"\mathcal " + name + r"(\alpha)", name + "_x")
        text = text.replace(r"a^{(k)}(\alpha)", "a_x^{(k)}")
        second = "d'_" if section == "the circle rule" else "dd_"
        text = re.sub(r"\\phi''\(Y_([abijx])\)", lambda m: second + m[1], text)
        text = re.sub(r"\\phi'\(Y_([abijx])\)", r"d_\1", text)
        text = re.sub(r"\\phi'\(Z_([abijx])\)", r"e_\1", text)
        text = text.replace(r"\mathcal T_{abij}", "T_{abij}")
    text = re.sub(r"H_([abijx])\^\{\(1\)\}", r"h_\1", text)
    text = re.sub(r"H_([abijx])\^\{\(2\)\}", r"H_\1", text)
    return re.sub(r"\s+", "", text)


def validate(original: str, result: str, editors: list[Editor]):
    old_sections = original.split(SECTION_MARKER)
    new_sections = result.split(SECTION_MARKER)
    display_checks = []
    for before, after, editor in zip(old_sections, new_sections, editors):
        # Reverse every concrete recorded replacement by location.
        restored = after
        for edit in reversed(editor.edits):
            for i, before_pos in reversed(list(enumerate(edit["before_offsets"]))):
                pos = before_pos + i * (len(edit["new"]) - len(edit["old"]))
                assert restored[pos:pos + len(edit["new"])] == edit["new"]
                restored = restored[:pos] + edit["old"] + restored[pos + len(edit["new"]):]
        assert restored == before, editor.section
        old = re.findall(r"\\\[(.*?)\\\]", before, re.S)
        new = re.findall(r"\\\[(.*?)\\\]", after, re.S)
        assert len(old) == len(new), editor.section
        for index, (a, b) in enumerate(zip(old, new), 1):
            assert display_canonical(a, editor.section) == display_canonical(b, editor.section), (editor.section, index, a, b)
            # Restrict changes to known notation-bearing displays; the inverse
            # normalization must not conceal changes to quadrature h_j, etc.
            tag = re.search(r"\\tag\{([^}]+)\}", a)
            changed_tags = {"C4.31", "C4.E2", "C4.E3", "C4.E7", "C4.E9",
                            "C4.A5", "C4.A6", "C4.A7", "C4.A8", "C4.D5"}
            changed_untagged = (editor.section == "the circle rule" and "F_x^{(k)}" in a) or (editor.section == "exact interval assembly" and "M_{bj}=p_j E[" in a)
            if not ((tag and tag[1] in changed_tags) or changed_untagged):
                assert a == b, ("unexpected display change", editor.section, index)
        display_checks.append(dict(section=editor.section, display_count=len(old),
                                   notation_normalized_identical=True, invertible_edit_map=True))
    tags = re.findall(r"\\tag\{([^}]+)\}", original)
    assert tags == re.findall(r"\\tag\{([^}]+)\}", result)
    assert len(tags) == len(set(tags))
    references = set(re.findall(r"C4\.(?:[AED])?\d+[a-z]?", result))
    assert references <= set(tags), references - set(tags)
    assert result.count(r"\[") == result.count(r"\]")
    assert result.count(r"\begin{aligned}") == result.count(r"\end{aligned}")
    assert result.count("`") % 2 == 0
    assert re.findall(r"```.*?```", original, re.S) == re.findall(r"```.*?```", result, re.S)
    original_keys = set(re.findall(r"\b(?:dynamic_\w+|\w+_bits)\b", original))
    assert original_keys == set(re.findall(r"\b(?:dynamic_\w+|\w+_bits)\b", result))
    assert re.findall(r"\]\(([^)]+)\)", original) == re.findall(r"\]\(([^)]+)\)", result)
    assert "E_4" not in result and "Delta(t)" not in result
    assert "lpha^(1)" not in result.replace("H_alpha^(1)", "")
    assert not re.search(r"\bE\[|`E (?:phi|S|H)", result)
    for word in ("conditional on inspection", "coordinator", "was found", "uninspected"):
        assert word not in result
    # Preserve all arithmetic/sign conclusions at the literal source level.
    for tag in ("C4.7", "C4.8a", "C4.8", "C4.32", "C4.33", "C4.34"):
        expression = r"\\\[((?:(?!\\\]).)*?\\tag\{" + re.escape(tag) + r"\}.*?)\\\]"
        assert re.search(expression, original, re.S)[0] == re.search(expression, result, re.S)[0], tag
    chi = (Fraction(5358604107658561212253567,19807040628566084398385987584),
           Fraction(21597479156841685713774185,79228162514264337593543950336))
    beta = (Fraction(2797504526179671494928101665,79228162514264337593543950336),
            Fraction(2797556156441557459457527739,79228162514264337593543950336))
    D8 = Fraction(41272525446939874982,31640625)
    angular = Fraction(20636262723469937491,127677049435953561600000000)
    assert Fraction(27,100000) < chi[0] <= chi[1] < Fraction(273,1000000)
    assert Fraction(35309,1000000) < beta[0] <= beta[1] < Fraction(35311,1000000) < Fraction(1,10)
    assert 16*D8/(7*256**8) == angular < Fraction(1,1000000)
    return dict(display_checks=display_checks, equation_tags=tags,
                resolved_C4_references=sorted(references), code_keys=sorted(original_keys),
                balanced_displays=result.count(r"\["),
                protocol_fences_unchanged=True, links_unchanged=True,
                literal_theorem_and_enclosure_unchanged=True,
                exact_rational_endpoint_and_angle_comparisons=True,
                no_coefficient_evaluation=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--check", action="store_true", help="Compare the existing V2 without rewriting it")
    args = parser.parse_args()
    output = args.output.resolve()
    generated = (ROOT / "data/generated/two_layer_test_risk").resolve()
    if not output.is_relative_to(generated) or output == generated:
        raise ValueError("Output must be a fresh directory in the study generated namespace")
    output.mkdir(parents=True, exist_ok=False)
    original = SOURCE.read_text()
    assert digest(original) == SOURCE_SHA256
    assert digest((HERE / "build_signed_candidate.py").read_text()) == BUILDER_SHA256
    result, editors = assemble(original)
    checks = validate(original, result, editors)
    if args.check:
        assert TARGET.read_text() == result, "Existing V2 differs from deterministic assembly"
    else:
        TARGET.write_text(result)
    edits = [edit for e in editors for edit in e.edits]
    (output / "editmap.json").write_text(json.dumps(edits, indent=2) + "\n")
    (output / "original_to_v2.diff").write_text("".join(difflib.unified_diff(
        original.splitlines(True), result.splitlines(True),
        fromfile="PROMOTION_SIGN_C4.md", tofile="PROMOTION_SIGN_C4_V2.md")))
    checks.update(source_sha256=digest(original), target_sha256=digest(result),
                  generator_sha256=digest(Path(__file__).read_text()),
                  original_builder_sha256=BUILDER_SHA256, edit_count=len(edits),
                  original_lines=len(original.splitlines()), target_lines=len(result.splitlines()))
    (output / "checks.json").write_text(json.dumps(checks, indent=2) + "\n")
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    main()
