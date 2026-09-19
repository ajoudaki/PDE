"""Study-owned general-activation adapter for the autonomous observable closure.

The dense smooth dictionary and its same-action Gaussian initializer do not
use the training activation. All moving and initial paired fields do use it.
No target trajectory, neural width, history or derivative above phi' is input.
See NUMERICAL_EXTENSION.md for conditional limits and resource accounting.
"""
from dataclasses import dataclass
from fractions import Fraction
import json

import numpy as np

from pde.observable_arithmetic import Arithmetic, gaussian_points
from pde.observable_compiler import compile_raw_dictionary
from pde.observable_initialization import InitializationLimits, InitializationResourceLimit
from pde.observable_solver import (
    State, DataLaw, ArcLaw, circle_inputs, state_bytes,
    _positive_integer, _unit_inputs,
    save_restart as _save_restart, load_restart as _load_restart,
    interpolate_state as _interpolate_state,
)
from pde.observable_words import decode_word


@dataclass(frozen=True)
class Activation:
    """Pure coordinatewise callbacks (array, Arithmetic) -> same-shaped array.

    The exact definition string identifies the fixed mathematical activation
    and evaluator version at restart. It is a caller declaration, not a proof
    that callbacks agree or are locally uniformly consistent as digits grow.
    C1,1, bounded slope, and those semantic obligations are the caller's.
    Callbacks receive private arrays; their outputs are copied and converted.
    """
    name: str
    definition: str
    value: object
    derivative: object
    evaluator_version: str = "1"

    def __post_init__(self):
        if not all(isinstance(s, str) and s for s in
                   (self.name, self.definition, self.evaluator_version)):
            raise ValueError("activation identifiers must be nonempty strings")
        if not callable(self.value) or not callable(self.derivative):
            raise TypeError("activation evaluators must be callable")

    def descriptor(self):
        return dict(name=self.name, definition=self.definition,
                    evaluator_version=self.evaluator_version)

    def evaluate(self, z, ar, derivative=False):
        if not isinstance(derivative, bool):
            raise ValueError("derivative selector must be boolean")
        source = ar.array(z)
        if not ar.finite(source):
            raise ValueError("nonfinite activation argument")
        with ar.context():
            result = ar.array((self.derivative if derivative else self.value)(source.copy(), ar))
        if result.shape != source.shape or not ar.finite(result):
            raise ValueError("activation evaluation must preserve shape and be finite")
        return result.copy()


TANH = Activation("tanh", "phi(z)=tanh(z)",
                  lambda z, ar: ar.tanh(z),
                  lambda z, ar: ar.real(1)-ar.tanh(z)**2)

LINEAR_SINE = Activation(
    "linear-sine", "phi(z)=z+sin(z)/4",
    lambda z, ar: z+ar.trig(z)/ar.real(4),
    lambda z, ar: ar.real(1)+ar.trig(z, cosine=True)/ar.real(4))


def _ramp(z, ar, derivative=False):
    zero, one, two = ar.real(0), ar.real(1), ar.real(2)
    result = ar.zeros(z.shape)
    for index in np.ndindex(z.shape):
        x = z[index]
        if x <= zero:
            result[index] = zero
        elif x >= one:
            result[index] = one if derivative else x-one/two
        else:
            result[index] = x if derivative else x*x/two
    return result


FLAT_RAMP = Activation(
    "flat-ramp", "phi(z)=0 for z<=0; z^2/2 for 0<z<1; z-1/2 for z>=1",
    _ramp, lambda z, ar: _ramp(z, ar, True))


@dataclass(frozen=True)
class Dictionary:
    order: int
    code_ceiling: int
    first_words: tuple
    second_words: tuple
    first_codes: tuple
    second_codes: tuple


def build_dictionary(order, *, limits=None):
    """All bounded valid codes <=16N; retain literal output duplicates.

    Dependencies have smaller codes. Cofinality gives exactly the smooth
    dense language in CLOSURE_PROOF.md, with the same ridge 2^-N.
    Resource limits reject a request; they never truncate its dictionary.
    """
    _positive_integer(order, "order")
    limits = limits or InitializationLimits()
    ceiling = 16*order
    if ceiling+1 > limits.max_codes:
        raise InitializationResourceLimit("dictionary code prefix exceeds max_codes")
    words, codes = [[], []], [[], []]
    nodes = set()
    for code in range(ceiling+1):
        word = decode_word(code)
        if word is None or not word.bounded:
            continue
        layer = word.population-1
        words[layer].append(word)
        codes[layer].append(code)
        if len(words[layer]) > limits.max_features_per_population:
            raise InitializationResourceLimit("retained dictionary exceeds feature allowance")
        stack = [word]
        while stack:
            node = stack.pop()
            if node in nodes:
                continue
            nodes.add(node)
            if len(nodes) > limits.max_dictionary_nodes:
                raise InitializationResourceLimit("dictionary exceeds node allowance")
            stack.extend(node.args)
    return Dictionary(order, ceiling, *map(tuple, words), *map(tuple, codes))


def _check_activation(state, activation):
    if not isinstance(activation, Activation):
        raise TypeError("supply one Activation for both layers")
    if state.metadata.get("activation") != activation.descriptor():
        raise ValueError("activation does not match the saved state descriptor")


def supplied_state(*, b1, g, w, p1, b2, c, p2, M, D, activation,
                   arithmetic=None, metadata=None):
    """Own a supplied finite state; this does not certify reachability."""
    ar = arithmetic or Arithmetic()
    record = json.loads(json.dumps(metadata or {}))
    record["activation"] = activation.descriptor()
    record.setdefault("provenance", "supplied state; reachability not asserted")
    def convert(value):
        a=np.asarray(value,dtype=object)
        exact=[Fraction(x) if isinstance(x,str) else x for x in a.flat]
        return ar.array(np.asarray(exact,dtype=object).reshape(a.shape)).copy()
    return State(*(convert(a) for a in (b1,g,w,p1,b2,c,p2,M,D)),
                 ar, record).validate()


def initialize(activation, order=1, *, initialization_nodes=256, population_nodes=128,
               digits=None, backend="decimal", epsilon_cov="0.001", limits=None):
    """Always the full generic Gaussian program, then frozen P-point replay.

    The initializer never evaluates activation.value or activation.derivative.
    All source responses and uncentered Grams use smooth dictionary probes.
    Q and P are joint integration counts, independent of neural width.
    """
    if not isinstance(activation, Activation):
        raise TypeError("activation must be an Activation")
    limits = limits or InitializationLimits()
    dictionary = build_dictionary(order, limits=limits)
    for count, name in ((initialization_nodes, "initialization_nodes"),
                        (population_nodes, "population_nodes")):
        _positive_integer(count, name)
        if count > limits.max_points:
            raise InitializationResourceLimit("integration count exceeds max_points")
    ar = Arithmetic(digits, backend)
    d1, d2 = len(dictionary.first_words), len(dictionary.second_words)
    # Full compiler has its separate preallocation guards. These cover the
    # subsequent transforms and state arrays as well as raw table outputs.
    slots = 12*(d1*d1+d2*d2+d1*d2)+(initialization_nodes+population_nodes)*(6*(d1+d2)+32)
    byte_estimate = slots*(8 if digits is None else 192+digits)
    work_estimate = (initialization_nodes+population_nodes)*4*(d1+d2)**2+4*(d1+d2)**3
    if byte_estimate > limits.max_working_bytes or work_estimate > limits.max_work_units:
        raise InitializationResourceLimit("normalization/state work or storage allowance exceeded")
    with ar.context():
        raw = compile_raw_dictionary(
            dictionary.first_words, dictionary.second_words,
            arithmetic=ar, gaussian_points=gaussian_points,
            initialization_nodes=initialization_nodes, population_nodes=population_nodes,
            epsilon_cov=epsilon_cov, limits=limits.compiler_limits)
        eta = ar.real(Fraction(1, 2**order))
        if eta <= 0:
            raise ValueError("positive feature ridge unresolved at working precision")
        t1 = ar.inverse_lower(ar.cholesky(raw.gram1+eta*ar.eye(d1)))
        t2 = ar.inverse_lower(ar.cholesky(raw.gram2+eta*ar.eye(d2)))
        b1, b2, D = raw.psi1 @ t1.T, raw.psi2 @ t2.T, t2 @ raw.C @ t1.T
        record = dict(
            activation=activation.descriptor(), dictionary_scheme="smooth-code-16N-v1",
            hierarchy_order=order, code_ceiling=dictionary.code_ceiling,
            retained_codes=[list(dictionary.first_codes), list(dictionary.second_codes)],
            feature_dimensions=[d1,d2], ridge_numerator=1, ridge_denominator=2**order,
            normalization="inverse-lower-Cholesky; orthogonal to symmetric coordinates",
            initialization_strategy="complete-gaussian-program",
            initialization_nodes=initialization_nodes, population_nodes=population_nodes,
            epsilon_cov=str(ar.real(epsilon_cov)), gaussian_rule="Halton-Box-Muller",
            exact_initialized_law=False, compiler=dict(raw.metadata),
            arithmetic_digits=digits, arithmetic_backend="float64" if digits is None else backend,
            estimated_normalization_bytes=byte_estimate,
            estimated_normalization_work=work_estimate,
            model="bias-free two-hidden-layer; normalized circle; same activation",
            finite_gaussian_variances=["1","1/n","1/n^2"],
            finite_mobilities=["n","1","n"], loss="unhalved probability mean squared",
            target_scope="conditional on applicable strong-target/tail/identification theorem")
        state = State(b1, raw.g, raw.g.copy(), raw.probabilities1, b2,
                      ar.zeros(population_nodes), raw.probabilities2,
                      D.copy(), D, ar, record).validate()
    # raw and its source program are not retained by the evolving state.
    return state


def law_quadrature(law, nodes_per_arc, arithmetic, **kwargs):
    """Represent a law without inheriting a tanh-only scope label.

    Accepts maintained ArcLaw and OrthogonalArcLaw (including custom radii).
    Metadata identifies geometry; target existence/tails remain external.
    """
    data = law.quadrature(nodes_per_arc, arithmetic, **kwargs)
    data.metadata = json.loads(json.dumps(data.metadata))
    # Preserve all geometric/rounding descriptors while superseding scope tags.
    for key in ("scope", "theorem_scope", "scientific_scope"):
        if key in data.metadata:
            data.metadata["upstream_"+key] = data.metadata.pop(key)
    data.metadata["scope"] = "general activation: fixed-order numerical law; target theorem required"
    return data.validate(arithmetic)


def _fields(state, inputs, activation, backward=True):
    ar = state.arithmetic
    z1 = state.w @ inputs.T
    h1 = activation.evaluate(z1, ar)
    a = state.b1.T @ (state.p1[:,None]*h1)
    z2 = state.b2 @ (state.M @ a)
    h2 = activation.evaluate(z2, ar)
    result = dict(z1=z1,h1=h1,a=a,z2=z2,h2=h2,
                  f=state.p2 @ (state.c[:,None]*h2))
    if backward:
        gate1 = activation.evaluate(z1,ar,True)
        delta2 = state.c[:,None]*activation.evaluate(z2,ar,True)
        d = state.b2.T @ (state.p2[:,None]*delta2)
        q = state.b1 @ (state.M.T @ d)
        result.update(gate1=gate1,delta2=delta2,d=d,q=q,delta1=gate1*q)
    if not all(ar.finite(x) for x in result.values()):
        raise ValueError("nonfinite closure field")
    return result


def fields(state, inputs, activation, *, backward=True):
    state.validate()
    _check_activation(state,activation)
    with state.arithmetic.context():
        return _fields(state,_unit_inputs(inputs,state.arithmetic),activation,backward)


def apply_action(state, input_population, values, *, frozen=False):
    """Finite action on supplied current observation columns; actual transpose."""
    state.validate()
    if isinstance(input_population,bool) or input_population not in (1,2):
        raise ValueError("input population must be 1 or 2")
    if not isinstance(frozen,bool):
        raise ValueError("frozen must be boolean")
    ar = state.arithmetic
    with ar.context():
        values = ar.array(values)
        source, target, weights = ((state.b1,state.b2,state.p1) if input_population==1
                                   else (state.b2,state.b1,state.p2))
        if values.ndim not in (1,2) or len(values)!=len(source):
            raise ValueError("action values must live on the declared population")
        matrix = state.D if frozen else state.M
        if input_population==2:
            matrix=matrix.T
        result=target @ (matrix @ (source.T @ (weights[:,None]*values if values.ndim==2 else weights*values)))
    if not ar.finite(result):
        raise ValueError("nonfinite action result")
    return result


def predict(state, inputs, activation, *, block_size=16):
    _positive_integer(block_size,"block_size")
    state.validate()
    _check_activation(state,activation)
    ar=state.arithmetic
    with ar.context():
        inputs=_unit_inputs(inputs,ar)
        result=ar.zeros(len(inputs))
        for start in range(0,len(inputs),block_size):
            result[start:start+block_size]=_fields(state,inputs[start:start+block_size],activation,False)["f"]
    return result


def rhs(state, data, activation, *, block_size=16):
    _positive_integer(block_size,"block_size")
    state.validate()
    _check_activation(state,activation)
    ar=state.arithmetic
    with ar.context():
        data.validate(ar)
        w,c,M=ar.zeros(state.w.shape),ar.zeros(state.c.shape),ar.zeros(state.M.shape)
        for start in range(0,len(data.inputs),block_size):
            stop=min(start+block_size,len(data.inputs))
            u=data.inputs[start:stop]
            v=_fields(state,u,activation)
            r=data.probabilities[start:stop]*(v["f"]-data.labels[start:stop])
            w-=2*(v["delta1"]*r) @ u
            c-=2*v["h2"] @ r
            M-=2*(v["d"]*r) @ v["a"].T
        if not all(ar.finite(x) for x in (w,c,M)):
            raise ValueError("nonfinite closure velocity")
    return w,c,M


def loss(state,data,activation,*,block_size=16):
    with state.arithmetic.context():
        data.validate(state.arithmetic)
        residual=predict(state,data.inputs,activation,block_size=block_size)-data.labels
        value=data.probabilities @ (residual*residual)
        if not state.arithmetic.finite(np.asarray([value])):
            raise ValueError("nonfinite loss")
        return value


def evolve(state,data,activation,*,steps,step_size,block_size=16):
    """Simultaneous Heun; finite-step stability is not promised."""
    _positive_integer(steps,"steps")
    _positive_integer(block_size,"block_size")
    _check_activation(state,activation)
    ar=state.arithmetic
    current=state.copy().validate()
    with ar.context():
        h=ar.real(step_size)
        if h<=0:
            raise ValueError("step_size must be positive")
        for _ in range(steps):
            k=rhs(current,data,activation,block_size=block_size)
            stage=current.dynamic_copy(current.w+h*k[0],current.c+h*k[1],current.M+h*k[2])
            l=rhs(stage,data,activation,block_size=block_size)
            current=current.dynamic_copy(current.w+(h/2)*(k[0]+l[0]),
                                         current.c+(h/2)*(k[1]+l[1]),current.M+(h/2)*(k[2]+l[2])).validate()
    return current


def interpolate_state(left,right,fraction):
    if left.metadata.get("activation")!=right.metadata.get("activation"):
        raise ValueError("interpolation requires the same activation")
    return _interpolate_state(left,right,fraction)


def paired_observations(state,data,activation,*,block_size=16,include_pairs=True):
    _positive_integer(block_size,"block_size")
    state.validate()
    _check_activation(state,activation)
    ar=state.arithmetic
    with ar.context():
        data.validate(ar)
        pairs=([ar.zeros((len(state.b1),len(data.inputs),2)),
                ar.zeros((len(state.b2),len(data.inputs),2))] if include_pairs else [None,None])
        sums=[ar.real(0),ar.real(0)]
        for start in range(0,len(data.inputs),block_size):
            stop=min(start+block_size,len(data.inputs))
            u=data.inputs[start:stop]
            v=_fields(state,u,activation,False)
            initial1=activation.evaluate(state.g @ u.T,ar)
            initial2=activation.evaluate(apply_action(state,1,initial1,frozen=True),ar)
            for layer,initial,current,p in ((0,initial1,v["h1"],state.p1),(1,initial2,v["h2"],state.p2)):
                sums[layer]+=p @ ((current-initial)**2) @ data.probabilities[start:stop]
                if include_pairs:
                    pairs[layer][:,start:stop,0]=initial
                    pairs[layer][:,start:stop,1]=current
        return dict(first_pairs=pairs[0],second_pairs=pairs[1],
                    first_weights=state.p1.copy(),second_weights=state.p2.copy(),
                    input_weights=data.probabilities.copy(),inputs=data.inputs.copy(),
                    rms1=ar.sqrt(sums[0]).item(),rms2=ar.sqrt(sums[1]).item())


def save_restart(path,state,data,activation):
    _check_activation(state,activation)
    _save_restart(path,state,data)


def load_restart(path,activation):
    state,data=_load_restart(path)
    _check_activation(state,activation)
    return state,data
