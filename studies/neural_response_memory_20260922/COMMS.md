# Research communications and outreach

Created: 2026-09-25. Owner: Amir; compiled in the outreach side conversation.
Updated: 2026-09-25, incorporating the ETH/Apple relationships and introduction
routes reported later in that conversation. A separate
[handoff prompt](COMMS_HANDOFF_PROMPT.md) resumes this communications task.

This file records the planned messages, contact priorities, and possible
introductions discussed with Amir. A prepared draft is not a record of sending.
Francesco Orabona's initial research message is confirmed sent by Amir.
Amir also reports already chatting with Antonio Orvieto; the subject, date and
outcome of that conversation were not specified. No messages were sent by the
assistant. Update status and dates when Amir reports contact.

The six previously prepared emails are preserved below. Their theorem statements
refer to the original activity-clock, two-hidden-layer tanh result. They are a
snapshot of the outreach wording, not a complete account of later study results.
Scientific sources remain the study's [README](README.md),
[original-clock proof](ORACLE_FINITE_HORIZON_BOUND.md), and experimental reports.
Study results are internally checked research, not promoted established material.

### Scientific wording before reusing a draft

The study has continued while these messages were being prepared. The current
README reports the following later results; this communications update has not
independently audited their proofs:

- [Response-clock finite-horizon theorem](RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md):
  O_T(P^-2) physical-trajectory tracking for sufficiently large P at fixed finite
  width, dataset and horizon, for the specified response-clock closure.
- [Fixed-depth activation extension](DEEP_ACTIVATION_ERROR_THEOREM.md):
  old-clock O_T(P^-1) and new-clock O_T(P^-2) results at every fixed finite
  hidden depth, under different smoothness conditions. Read the full theorem
  before naming covered activations or asserting existence for every order.
  Literal ReLU/SELU crossings remain a separate nonsmooth issue.
- [Scalar compression assessment](SCALAR_COMPRESSION_BOUND_ASSESSMENT.md):
  a further, distinct compression level, including a stabilized scalar variant.
  Do not fold this into the population-history claim without explaining the
  changed algorithm and the second cutoff parameter.

Before preparing a current scientific attachment or updating an email's theorem,
read the README and the complete relevant statement/proof/corrections within
this study. Keep theory, implemented algorithms, experiments, and internal
check status distinct. In particular, the new deep response-clock construction
is reported as not yet implemented or experimentally tested. The phrase
"errors remain stable over the whole training" in the already-sent Orabona
message should be made precise in any follow-up: the guarantees discussed here
are for prescribed finite horizons, not uniform over all time. The saved emails
below remain historical drafts rather than an automatically updated abstract.

## First circle: existing drafts and confirmed relationships

“Draft ready” means the text is prepared; sending has not been confirmed.

| Person | Relationship reported by Amir | Status | Main purpose |
| --- | --- | --- | --- |
| Francesco Orabona | Former colleague | Initial message sent; exact send date not recorded | Scientific discussion and presentation advice; already handled, no draft repeated here |
| Vincent Fortuin | Friend | Draft ready | Perspective, related work, and presentation |
| Francis Bach | PhD co-advisor | Draft ready | Mathematical assessment, positioning, and possible introductions |
| Mehrdad Farajtabar | Amir knows him; coauthor on the ICLR 2026 plasticity paper | Original draft ready; updated opening below; sending not confirmed | Scientific feedback, connection to shared plasticity work, and possible Apple/EPFL introductions |
| Francesco Locatello | Former labmate | Draft ready | Connections to initialization and feature learning; positioning |
| Fanny Yang | Has been close with Amir at various points | Draft ready | Overparameterized models and representation dynamics |
| Niao He | Has been close with Amir at various points | Draft ready | Approximation, stability, and optimization theory |
| Thomas Hofmann | Amir works in his group; coauthor | No outreach status reported | Local scientific framing, presentation, and introduction advice |
| Lorenzo Noci | Amir is very close to him; explicitly first circle | No outreach status reported | Early technical reader; possible introduction to Boris Hanin |
| Aurélien Lucchi | Explicitly first circle | No outreach status reported | Optimization dynamics, stability, and positioning |
| Antonio Orvieto | Existing contact | Amir has already chatted with him; topic/outcome unspecified | Optimization and sequence-memory perspective; possible introduction to Albert Gu |
| Lénaïc Chizat | Amir knows him | No message prepared here | Gradient-flow assessment and advice on EPFL readers |
| Blake Bordelon | Amir knows him | No message prepared here | Dynamical mean-field theory; possible introductions to Boris or Cengiz |
| Andrew Saxe | Amir thinks he has a good connection | No message prepared here | Representation dynamics and useful scientific demonstrations |
| Giulia Lanzillotta | Verified coauthor on the ICLR 2026 paper; personal closeness not specified | No outreach status reported | Feedback on the relationship to the shared plasticity work |
| Mohammad Samragh Razlighi | Apple coauthor on that paper; individual closeness not specified | No outreach status reported | Shared training-dynamics context and practical questions |
| Iman Mirzadeh | Apple coauthor on that paper; individual closeness not specified | No outreach status reported | Continual-learning relevance and experimental framing |
| Keivan Alizadeh / Alizadeh-Vahid | Apple coauthor on that paper; individual closeness not specified | No outreach status reported | Shared plasticity context and practical relevance |
| Fartash Faghri | Apple coauthor on that paper; individual closeness not specified | No outreach status reported | Scientific feedback and possible Apple discussion/seminar route |

This table records existing relationships, not equal closeness or an instruction
to contact everyone. Coauthorship is verified below; only Amir can specify how
close each collaboration is.

Name distinctions: Francesco Orabona and Francesco Locatello are different
contacts. The spellings Vincent Fortuin and Francesco Locatello were verified
against their public profiles.

## Second circle: additional contacts

These are additional potential readers. Directly known contacts are listed
above; public professional links below suggest possible introductions but do
not establish a personal relationship with Amir.

| Person | Connection status | Why contact them / proposed question | Next step |
| --- | --- | --- | --- |
| Boris Hanin | Amir explicitly likes this suggestion; no direct relationship confirmed | Quantitative training dynamics; assess the approximation theorem and which dependencies matter | High priority; ask Lorenzo, or alternatively Blake, about an introduction |
| Etai Littwin | No direct relationship or mutual-coauthor route confirmed | Tensor Programs and feature-learning dynamics; compare the closure with existing descriptions of training | High priority; ask Mehrdad or another Apple collaborator whether they know him |
| Emmanuel Abbé (EPFL) | No direct relationship confirmed; verified coauthor of Mehrdad | Learnability by gradient methods and feature-learning theory; assess positioning and useful consequences | High-priority EPFL addition; ask Mehrdad about an introduction |
| Samy Bengio | No direct relationship confirmed; verified coauthor of Mehrdad | Broader scientific framing and identifying interested Apple researchers | Ask Mehrdad whether a discussion or introduction would be useful |
| Andrea Montanari | Added explicitly by Amir; personal relationship not specified | Quantitative descriptions of training and mean-field limits; assess the distinction between fixed-width history compression and large-width reduction | New draft included below; decide whether direct contact or an introduction is preferable |
| Cengiz Pehlevan | No personal connection confirmed | Deep feature-learning dynamics and response/correlation histories | Possible introduction through Blake, his documented coauthor; avoid duplicating the same request without a purpose |
| Albert Gu | No personal connection confirmed | HiPPO and polynomial history compression; clarify inherited machinery versus the autonomous neural coupling | Prefer asking Antonio, his documented coauthor; the longer Mehrdad–Razvan route remains a fallback |
| Tri Dao | No personal connection confirmed | HiPPO coauthor; complementary or alternative reader for history compression | Select a clear technical question before contacting; no introduction route established here |
| Eric Vanden-Eijnden | No direct personal connection confirmed | Dynamical approximation and stability; assess stronger comparison or long-time tools | Ask Francis or Chizat whether an introduction makes sense; longer documented route through Andrew and Stefano Sarao Mannelli |
| Song Mei | No direct personal connection confirmed | Quantitative approximation guarantees and dimension dependence | Ask Francis about an introduction; Song visited SIERRA in 2019 |
| Nicolas Flammarion (EPFL) | No personal connection confirmed; Francis was one of his PhD advisors | Gradient-flow trajectories, implicit bias, and saddle-to-saddle dynamics; assess the construction and which sharper guarantee would matter most | High-priority EPFL addition; ask Francis about an introduction; message not yet drafted |
| Lenka Zdeborová (EPFL) | No personal connection confirmed | Statistical physics of learning and dynamical mean-field memory; identify phenomena this history compression could help explain | High-priority EPFL addition; ask Chizat about an introduction or suitable group discussion; message not yet drafted |
| Florent Krzakala (EPFL) | No personal connection confirmed | Rigorous dynamical mean-field theory and reductions of SGD to tractable equations; assess finite-width versus population-level descriptions | High-priority EPFL addition; initially select Lenka or Florent according to the specific question; message not yet drafted |
| Clément Hongler (EPFL) | No personal connection confirmed | Mathematical descriptions of training, finite-width behavior, evolving kernels, and feature learning | Additional theoretical reader; ask Chizat about fit and a possible introduction; message not yet drafted |
| Martin Jaggi (EPFL) | No personal connection confirmed | Optimization and low-rank gradient compression; assess baselines and practical storage/computation benefits | Further algorithmic contact; prepare an accuracy-versus-cost comparison before outreach; message not yet drafted |
| Volkan Cevher (EPFL) | No personal connection confirmed | Optimization theory and methods for machine learning; assess guarantees and the path to a useful training algorithm | Further algorithmic contact; formulate a specific optimization question; message not yet drafted |

Stefano Sarao Mannelli and Razvan Pascanu are possible intermediaries in the
routes below. They are not recorded as people Amir already knows.

### Evidence for possible introductions

These are documented professional links, not guarantees of personal closeness
or willingness to introduce. Public sources were checked on 2026-09-25.

- **Amir → Francis → Song Mei:** the
  [2019 SIERRA report](https://radar.inria.fr/rapportsactivite/RA2019/sierra/uid1.html)
  lists Francis as team leader and Song as a visiting scientist in
  September–October 2019.
- **Amir → Francis or Chizat → Eric:** all three appear as university partners
  in the [Flatiron Mathematics of Deep Learning initiative](https://www.simonsfoundation.org/flatiron/center-for-computational-mathematics/machine-learning-and-data-analysis/mathematics-and-science-of-deep-learning/).
  This is a reason to ask whether they know Eric, not proof of a close relationship.
- **Amir → Andrew → Stefano Sarao Mannelli → Eric:**
  [Stefano's CV](https://stefsmlab.github.io/assets/docs/people/stef-CV-2024-01.pdf)
  records Andrew as his postdoctoral supervisor and a research visit with Eric.
- **Amir → Mehrdad → Razvan Pascanu → Albert:** Mehrdad and Razvan coauthored
  [Linear Mode Connectivity in Multitask and Continual Learning](https://research.google/pubs/linear-mode-connectivity-in-multitask-and-continual-learning/);
  Razvan and Albert coauthored
  [Resurrecting Recurrent Neural Networks for Long Sequences](https://arxiv.org/abs/2303.06349).
- **Amir → Antonio → Albert:** Antonio and Albert coauthored that same
  [LRU paper](https://arxiv.org/abs/2303.06349). Given Amir's reported contact
  with Antonio, this is the shorter documented route.
- **Amir → Lorenzo or Blake → Boris:** all three coauthored
  [Depthwise Hyperparameter Transfer in Residual Networks: Dynamics and Scaling Limit](https://arxiv.org/abs/2309.16620),
  also with Cengiz Pehlevan and Mufan Bill Li. Choose one introduction route
  initially rather than asking several people to approach Boris simultaneously.
- **Amir → Mehrdad → Emmanuel Abbé or Samy Bengio:** all three coauthored
  [RL for Reasoning by Adaptively Revealing Rationales](https://machinelearning.apple.com/research/rl-for-reasoning).
- **Etai → Greg Yang:** their joint
  [Tensor Programs IIb paper](https://machinelearning.apple.com/research/tensor-programs)
  provides a potential later route if a useful discussion with Etai develops.
  An introduction from Amir's Apple collaborators to Etai is still unverified.
- **Amir → Blake → Cengiz:** Blake and Cengiz coauthored
  [Disordered Dynamics in High Dimensions](https://arxiv.org/abs/2601.01010).
- **Song → Andrea Montanari:** they coauthored
  [Mean-field theory of two-layers neural networks: dimension-free bounds and kernel limit](https://arxiv.org/abs/1902.06015).
  This is a possible further route if contact with Song develops, not an
  established personal connection between Amir and Andrea.

### EPFL priorities and sources

Added at Amir's request on 2026-09-25. Chizat was already on the list and is
already known to Amir. The suggested first EPFL conversations are Chizat,
Flammarion, and either Zdeborová or Krzakala. Hongler is another close theoretical
fit; Jaggi and Cevher add algorithmic and computational perspectives. These
priorities are recommendations, not confirmed plans or inferred personal ties.
The later discovery of Mehrdad's direct coauthorship with Emmanuel Abbé adds
Abbé to the high-priority EPFL group; he was absent from the original list.

- **Nicolas Flammarion:** his [EPFL biography](https://graphsearch.epfl.ch/en/person/317566)
  records Francis Bach and Alexandre d’Aspremont as his PhD advisors, giving a
  documented possible introduction route through Francis. His
  [group publications](https://www.epfl.ch/labs/tml/theory-of-machine-learning/publications/)
  include work on learning trajectories and saddle-to-saddle dynamics.
- **Lenka Zdeborová and Florent Krzakala:** see Zdeborová's
  [research profile](https://www.epfl.ch/labs/spoc/prof-lenka-zdeborova/),
  Krzakala's [lab](https://www.epfl.ch/labs/idephics/), and their joint
  [rigorous DMFT paper](https://arxiv.org/abs/2210.06591), which explicitly
  describes the buildup of memory kernels. Krzakala also coauthored
  [a reduction of SGD dynamics to dimensionless ODEs](https://arxiv.org/abs/2302.05882).
- **Clément Hongler:** his [group publications](https://www.epfl.ch/labs/csft/publications/)
  cover the NTK, feature learning, and finite-width neural-network theory.
- **Martin Jaggi:** [profile](https://people.epfl.ch/martin.jaggi?lang=en) and
  [PowerSGD research](https://ecocloud.epfl.ch/research/sustainable-society/powersgd/).
  Gradient communication compression and the study's training-history
  compression have different objectives; the connection is useful for
  discussing baselines and practical benefits.
- **Volkan Cevher:** [research profile](https://www.epfl.ch/labs/lions/people/volkan-cevher/)
  lists optimization theory and methods and machine learning.

Ask Chizat which colleagues would be most interested after he has seen the
short note. An EPFL seminar followed by a few focused technical discussions
is a possible outreach format; no invitation or visit has been arranged.

### Apple collaborators and the shared plasticity paper

Amir identified himself as Amir Joudaki and asked to check his ICLR paper.
[The official ICLR 2026 record](https://proceedings.iclr.cc/paper_files/paper/2026/hash/511c7fd69db9f1ce7492a57285975849-Abstract-Conference.html)
and [Apple's publication page](https://machinelearning.apple.com/research/barriers-for-learning)
verify *Barriers for Learning in an Evolving World: Mathematical Understanding
of Loss of Plasticity*. The paper lists Amir, Giulia Lanzillotta, Mohammad
Samragh Razlighi, Iman Mirzadeh, Keivan Alizadeh, Thomas Hofmann, Mehrdad
Farajtabar, and Fartash Faghri. The proceedings use shorter/alternate forms of
Mohammad's and Keivan's surnames. Its introduction and authorship were checked
for outreach; this conversation did not conduct a full proof review.

The paper analyzes loss of plasticity through invariant structures of training
dynamics, including frozen and cloned units. This is a natural shared scientific
context for the new work. A useful question for these coauthors is whether a
controlled reduced description can preserve diagnostics of approach to these
structures and their stability. That is a proposed application, not a result
already established by the closure theorem. History-memory compression and
representational rank collapse are different operations; avoid conflating them.

Specific additional Apple-related readers:

- **Etai Littwin:** [Tensor Programs IIb](https://machinelearning.apple.com/research/tensor-programs)
  and [feature learning with bottlenecks](https://arxiv.org/abs/2107.00364)
  make him a particularly relevant technical reader. His papers are evidence
  of fit, not evidence that Mehrdad personally knows him.
- **Oncel Tuzel:** a possible discussion/seminar contact through Fartash or
  Mehrdad. They have [coauthored together](https://openaccess.thecvf.com/content/ICCV2023/html/Faghri_Reinforce_Data_Multiply_Impact_Improved_Model_Accuracy_and_Robustness_with_ICCV_2023_paper.html).
  Prefer asking a collaborator who would find the work interesting before
  requesting an Apple talk; no invitation is implied.
- **Reserve technical readers, not immediate outreach:** Eran Malach has
  [joint work on state-space models with Etai](https://arxiv.org/abs/2510.14826).
  Noam Razin's [work on rank and implicit regularization](https://arxiv.org/abs/2408.02111)
  suggests a scientific fit; his [Apple collaboration with Etai and others](https://machinelearning.apple.com/research/vanishing-gradients-reinforcement)
  is a possible later route, not a confirmed connection to Amir.

Another route discussed earlier is **Hadi Daneshmand**, a verified coauthor of
Amir on [the ICLR 2024 batch-normalization paper](https://openreview.net/forum?id=xhCZD9hiiA).
His collaboration with Jason D. Lee and Chi Jin on
[particle gradient descent](https://arxiv.org/abs/2302.04753) suggests further
possible theory readers. Personal closeness and willingness to introduce have
not been reported. Keep these as reserve options rather than expanding the
immediate outreach wave.

## Outreach approach

1. Start with a manageable group of existing contacts and a specific scientific
   question for each. Francis, Lorenzo, Aurélien, Mehrdad, Chizat, Blake, and
   Andrew provide complementary perspectives and are already known to Amir.
   Select a few rather than contacting all of them at once.
2. Prepare a two-page note with the construction, precise theorem, one useful
   experiment, and related work; keep the full proof separate. This file does
   not claim that such an outreach note has already been prepared.
3. Make the storage/accuracy comparison concrete: error versus memory order,
   actual moving-state size, retained dense initialization, and sample-count
   dependence. Identify the particular clock, architecture, activation and
   solver behind each theorem and experiment; evidence for one is not evidence
   for every variant.
4. Discuss the connection to
   [HiPPO](https://proceedings.neurips.cc/paper_files/paper/2020/file/102f0bb6efb3a6128a3c750dd16729be-Paper.pdf)
   explicitly. Polynomial history compression is existing machinery; ask readers
   to assess the neural coupling, feedback analysis, and resulting guarantees.
5. Seek scientific judgment, then positioning and introductions. A useful ask:
   “What would most change your assessment of this result: a sharper theorem,
   a particular experiment, or a clearer connection to existing work?”
6. After useful feedback, consider a small technical seminar and a shareable
   preprint/example/figure. One friendly follow-up after about one or two weeks
   is reasonable. No outreach dates or meetings are scheduled here.

Core wording:

> We construct an autonomous history-moment approximation of nonlinear
> neural-network training and prove convergence to the dense gradient-flow
> trajectory as the memory order increases.

Attach the theorem's fixed-width, finite-horizon, architecture and activation
scope when stating it. The six original drafts below use the original-clock
result; new-clock results should be incorporated only through a deliberate
revision based on their full statement. No universal speedup, all-time tracking,
or elimination of the initialized dense matrices is claimed in these drafts.

Introduction request:

> I think this might also interest [name]. Do you know them well enough that an
> introduction would make sense? I can send you a short paragraph to forward.

### Suggested next wave and preparation

These are recommendations, not messages sent or commitments by Amir.

1. **Lorenzo:** ask for his own reaction and, if he sees a fit, an introduction
   to Boris. A strong technical conversation is the immediate goal.
2. **Mehrdad:** send the personal update referencing the shared plasticity work.
   After his reaction, ask about Etai and/or Emmanuel; do not load the first
   message with several introduction requests.
3. **Francis:** seek mathematical positioning and the most important missing
   comparison. His existing draft needs a scientific-scope refresh before reuse.
4. **Aurélien or Chizat:** choose a complementary optimization/gradient-flow
   reader, depending on availability. A local discussion may be enough.
5. **Antonio:** build on the conversation already held if relevant; ask about
   Albert for a specific history-compression comparison. Do not imply Antonio
   has already reviewed this result.

Blake and Andrew remain strong alternatives when the immediate question concerns
DMFT or representation dynamics. Montanari remains explicitly requested by Amir;
prepare a particularly clear short note before approaching him. Do not postpone
existing conversations simply to complete this suggested sequence.

Prepare one reusable two-page note: (1) the precise problem and what is being
compressed, (2) a compact diagram/equation for the autonomous feedback, (3) the
current theorem with its quantifiers, (4) one representative accuracy-versus-cost
figure with sample count and initialization storage visible, and (5) a short
related-work paragraph including HiPPO, training-dynamics limits and low-rank
methods. Link the complete technical report separately. No two-page note, talk,
or new plot is claimed to exist from this communications task.

For presentation, lead with controlled approximation of nonlinear training
dynamics. Then explain what memory compression buys in the tested setting.
Avoid claiming a breakthrough, universal speedup, or an all-time guarantee in
the outreach itself. Preserve Amir's enthusiasm through specific results and
an interesting question. Ask for scientific feedback before asking for help
with broader visibility. A focused seminar can follow once a reader sees a fit.

### Reusable personal openings and introduction requests

All of the following are unsent alternatives, not replacements for the saved
email text. They intentionally avoid exact rates until the current theorem is
selected and checked for the attachment.

**Apple coauthor opening (especially Mehrdad):**

> Following our plasticity work, I've been developing a way to describe nonlinear
> training dynamics using a finite set of evolving memory variables, with
> finite-time approximation guarantees. I'd really value your take—especially
> on whether this could become a useful tool for studying the training dynamics
> behind plasticity loss. Would you be up for a chat? Happy to send a short note.

**Lorenzo, after sharing the work:**

> I'd also be really interested in Boris's take on the approximation theorem.
> If you think it's a good fit, would you feel comfortable introducing us?
> I can send you a short paragraph to forward.

**Mehrdad, after his reaction:**

> Etai's work on training dynamics looks particularly relevant to this. Do you
> know him well enough that an introduction would make sense? I also noticed
> your paper with Emmanuel Abbé and would value your sense of whether this
> would interest him.

**Antonio, when following up on a relevant discussion:**

> I'd really like to understand how this relates to the polynomial-memory
> viewpoint behind HiPPO. Do you think Albert would be interested in looking
> at a short note, and would you be comfortable introducing us?

**Forwardable paragraph, to accompany a current short note:**

> Amir Joudaki, who works in Thomas Hofmann's group and was co-advised by Francis
> Bach during his PhD, has been developing an autonomous approximation of
> nonlinear neural-network training. It represents learned weight updates
> through evolving history moments while retaining the initialized matrices
> exactly. The work includes finite-horizon convergence guarantees as the
> memory order increases, at fixed finite width. He is looking for feedback
> on the construction, its relation to existing training-dynamics descriptions,
> and which consequences would be most useful to investigate.

For an email rather than a forwarded introduction, change the paragraph into
Amir's first-person voice. Check the attached note's scientific scope and avoid
including unpublished material beyond what Amir chooses to share.

## Prepared emails

### Vincent Fortuin

Personalization sources: [profile](https://fortuinlab.github.io/author/vincent-fortuin/)
and [ERC announcement](https://www.utn.de/en/2026/09/09/erc-starting-grant-for-utnprofessor-vincent-fortuin/).

~~~text
Subject: Catching up + a research idea I’d love your thoughts on

Hey Vincent,

How’s everything going? I just saw the news about your ERC grant—congratulations! :)

I wanted to tell you about a deep-learning theory project I’ve been working on for the past 2–3 years and get your thoughts.

The idea is to compress the history of training into a few evolving, width-sized memory vectors per training sample. These represent the learned part of the dense layers while keeping the initialization exact. This gives an autonomous approximation of the nonlinear training dynamics, with a proof of convergence as the memory order increases—currently for two hidden tanh layers over finite time intervals. Experiments on deeper networks with feature learning are encouraging too.

I’m really excited to get this out, and I’d love your perspective on the results, connections you see to other work, and how best to present them. Would you be up for a chat sometime?

Cheers,
Amir
~~~

### Francis Bach

Relationship and tone: Amir's PhD co-advisor; emphasize the precise theorem.

~~~text
Subject: Catching up and some new results on neural-network training

Hi Francis,

I hope you’re doing well!

I wanted to share some results from a direction I’ve been pursuing over the past 2–3 years. I’m quite excited about it and would really value your thoughts.

The idea is to compress the history of forward and backward responses during training into a finite set of evolving memory vectors per training sample. These represent the learned part of the dense layers, while retaining the initialized matrices exactly, and give an autonomous dynamical system.

For gradient flow in two-hidden-layer tanh networks, I have a proof of convergence to the dense training trajectory, with an O(1/P) error bound on any fixed finite time interval at fixed width, where P is the memory order. Experiments on deeper networks with feature learning are also encouraging.

I’d love your take on the construction, any connections to existing work that I might be missing, and how best to frame the results. Would you have time for a chat in the coming weeks? I’d be happy to send a short write-up beforehand.

Best,
Amir
~~~

### Mehrdad Farajtabar

Personalization source: [profile and research interests](https://sites.google.com/view/mehrdad).

~~~text
Subject: Catching up + some research I’d love your thoughts on

Hey Mehrdad,

How’s everything going?

I wanted to share a direction I’ve been working on for the past 2–3 years. Given your work on training dynamics, I thought you might find it interesting.

The idea is to compress the history of neural-network training into a few evolving, width-sized memory vectors per training sample. These represent the learned part of the dense layers while retaining the initialization exactly, giving an autonomous approximation of the nonlinear training dynamics.

There’s now a proof that increasing the memory order recovers the full gradient-flow trajectory over finite time intervals—currently for two hidden tanh layers. Experiments on deeper networks with feature learning are also encouraging.

I’m quite excited to get this out and would love your take on the results, any connections you see, and how best to frame the work. Would you be up for a chat sometime? Happy to send a short write-up beforehand.

Cheers,
Amir
~~~

### Francesco Locatello

Personalization sources: [profile](https://www.francescolocatello.com/) and
[initialization / fine-tuning paper](https://arxiv.org/abs/2602.20062).

~~~text
Subject: Catching up + some training-dynamics results

Hey Francesco,

How’s everything going at ISTA? :)

I wanted to tell you about a direction I’ve been working on for the past 2–3 years and get your thoughts.

The idea is to compress the history of neural-network training into a few evolving, width-sized memory vectors per training sample. These represent the learned part of the dense layers while keeping the initialization exact, giving an autonomous system that approximates the full nonlinear training dynamics.

I now have a finite-time convergence proof as the memory order increases, currently for two hidden tanh layers. Experiments on deeper networks with feature learning are also encouraging.

Given your recent work on initialization and feature learning during fine-tuning, I’d be especially curious whether you see useful connections here. I’m really excited to get this out and would also love your advice on how to frame the results and get them in front of the right people.

Would you be up for a chat sometime? Happy to send a short write-up beforehand!

Cheers,
Amir
~~~

### Fanny Yang

Personalization source: [profile and research interests](https://sml.inf.ethz.ch/group/fannyy/).

~~~text
Subject: Catching up + some new results on neural-network training

Hey Fanny,

How have you been? I wanted to catch up and share some results from a direction I’ve been pursuing over the past 2–3 years.

The idea is to compress the history of neural-network training into a few evolving, width-sized memory vectors per training sample. These represent the learned part of the dense layers while retaining the initialization exactly, giving an autonomous approximation of the nonlinear training dynamics.

I now have a proof of convergence as the memory order increases—currently for two hidden tanh layers over finite time intervals—and encouraging experiments on deeper networks with feature learning.

Given your work on overparameterized models, I’d really value your perspective on whether this could be a useful tool for understanding how representations evolve during training. I’m excited to get the results out and would also love your advice on how best to frame them.

Would you have time for a chat sometime? It would be lovely to catch up too!

Best,
Amir
~~~

### Niao He

Personalization source: [profile and research interests](https://odi.inf.ethz.ch/people/niao-he/).

~~~text
Subject: Some training-dynamics results I’d love your thoughts on

Hey Niao,

How’s everything going? I wanted to reconnect and tell you about a project I’ve been working on for the past 2–3 years.

I’ve developed an autonomous approximation of neural-network gradient flow that represents the learned part of the dense layers using evolving memory vectors, while keeping the initialization exact. The vectors summarize the history of forward and backward responses, with a tunable memory order.

For two-hidden-layer tanh networks at fixed width, I have an O(1/P) trajectory-error bound on any fixed finite time interval, where P is the memory order. The analysis controls the accumulated compression error and its feedback through the training dynamics. Experiments on deeper networks with feature learning are also encouraging.

I’d really love your take on the construction and the bounds, and your advice on how to frame the work for the optimization and ML theory community.

Would you be up for a chat in the coming weeks? Happy to send a short write-up beforehand—and it would be great to catch up!

Best,
Amir
~~~

### Andrea Montanari — additional draft

Added with this file at Amir's request to include Montanari in the outreach plan.
No previous personal relationship is assumed. Sources:
[Stanford profile](https://statistics.stanford.edu/people/andrea-montanari) and
[quantitative mean-field approximation paper](https://arxiv.org/abs/1902.06015).
This draft uses the same original-clock theorem as the earlier emails.

~~~text
Subject: An autonomous history-moment approximation of neural-network training

Dear Andrea,

I’m Amir, a former PhD student co-advised by Francis Bach. I wanted to share some results on nonlinear neural-network training and ask for your perspective, given your work on mean-field descriptions and quantitative approximation guarantees.

The construction represents the learned part of the dense hidden layers through a finite set of evolving history moments of forward and backward responses, while retaining the initialized matrices exactly. The resulting system is autonomous, with a tunable memory order P.

For two-hidden-layer tanh networks at fixed finite width, I have an O(1/P) bound on the discrepancy from the dense gradient-flow trajectory on any prescribed finite time interval. The proof controls accumulated compression error and its feedback into the dynamics. Experiments on deeper networks with feature learning are also encouraging.

I’d particularly value your thoughts on how this relates to existing descriptions of training dynamics, and what dependence on width, sample count, and time would make the result most informative. Would you be interested in seeing a short note? I’d also be very happy to discuss it if you have time.

Best,
Amir
~~~

## Follow-up record

| Person / event | Confirmed state | Date / next action |
| --- | --- | --- |
| Francesco Orabona | Initial research message sent by Amir | Exact send date not recorded; no further action assumed |
| Antonio Orvieto | Amir reports already chatting | Date, topic and outcome unspecified; do not label as a review of this study |
| Lorenzo Noci and Aurélien Lucchi | First-circle relationships confirmed | New messages not confirmed sent |
| Mehrdad and the other Apple coauthors | Existing collaboration verified; Amir reports knowing several Apple researchers | Drafts/openings only; no new outreach confirmed |
| All other prepared emails and introduction ideas | Sending, introductions and meetings unconfirmed | Update only from Amir's report or a specifically authorized action |

For each future update, record recipient, actual date, what was shared, response,
and agreed next step. A friendly follow-up after roughly 7–14 days is a
suggestion, not an automatic reminder or authorization to send. No assistant
messages, introductions, public posts, seminar invitations or automations have
been sent or created in this conversation.
