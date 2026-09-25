# Prompt for a new communications-strategy task

Copy the text below into a new Codex task in `/home/amir/Codes/PDE`.
It resumes the outreach work from Amir's side conversation, not the scientific
research tasks running in the shared checkout.

Communications checkpoint, 2026-09-25: COMMS.md now also contains a dated
continuation with source-reconciled wording, proposed messages for
Mehrdad, Francis and Aurélien, a Chizat alternative, a revised reserve
Montanari message, introduction requests, a two-page brief outline, and a factual
contact log. Start with that continuation while retaining the earlier history.
The theorem sources were read for messaging, not independently audited; the
MNIST100 report was read, not reproduced. No standalone brief or new figure
has been created. Amir then clarified that he has just messaged Lorenzo and
Francesco Orabona (2026-09-25), talked with Antonio, and discussed the work at
length with Thomas, but essentially no one else. The log records those events;
message contents, attachments, substantive replies and agreements are unknown.
Lorenzo's opening draft is preserved as preparation history, not the sent text
or a new message to send. The next unsent wave is Mehrdad, Francis and Aurélien.
All assistant-prepared messages remain unsent by the assistant.

---

Help me continue the communications and outreach strategy for my neural-network
training-dynamics research. My name is **Amir Joudaki**. This handoff comes from
an earlier side conversation; use the saved documents rather than assuming
you have that chat's full contents.

Read the current `/home/amir/Codes/PDE/AGENTS.md` and the applicable shared
workflow instructions. Your working record is:

`/home/amir/Codes/PDE/studies/neural_response_memory_20260922/COMMS.md`

Read that file completely. It contains the prepared emails, corrected contact
circles, sources for introduction routes, priorities, reusable openings, and
actual outreach status. Maintain it as the communications record. You may
update COMMS.md and this handoff prompt for the communications task. Preserve
historical drafts and clearly label proposed revisions and actual sending.
Do not change the scientific README, proofs, code, experiments, or other studies.
Do not stage, commit, reset, create worktrees, or disturb concurrent work.
No subagents are needed for this communications task.

## Goal and tone

Help me get useful scientific feedback, present the contribution clearly, and
reach the researchers most likely to understand or use it. I am excited about
the work and have been pursuing the direction for 2–3 years. Keep messages
friendly, brief, natural, and tailored to the relationship. Avoid hype, generic
flattery, and long lists of famous names. Prefer a few purposeful conversations
and warm introductions. Do not describe the work as a proven breakthrough.

## Scientific context and version caution

The central construction compresses histories of forward/backward responses
into evolving width-sized memory vectors per sample. These represent the learned
part of internal dense matrices; initialized matrices and their transpose actions
remain exact. The closure supplies its own responses and feedback, giving an
autonomous approximation to dense nonlinear gradient-flow training.

The earlier saved emails describe the original activity-clock result for two
hidden tanh layers, with O_T(P^-1) trajectory error at fixed finite width on a
prescribed finite horizon. They are historical drafts, not the current abstract.

Read the current study README before recommending new scientific wording:

`/home/amir/Codes/PDE/studies/neural_response_memory_20260922/README.md`

At this handoff, it reports newer results in:

- `ORACLE_FINITE_HORIZON_BOUND.md`: original-clock finite-horizon comparison.
- `RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md`: response-clock O_T(P^-2) comparison
  for sufficiently large P.
- `DEEP_ACTIVATION_ERROR_THEOREM.md` and `DEEP_ACTIVATION_SCOPE.md`: fixed-depth
  extensions with distinct smoothness assumptions and nonsmooth limitations.
- `SCALAR_COMPRESSION_BOUND_ASSESSMENT.md`: a separate scalar compression
  level and stabilized variant, with another cutoff parameter.

These files are in the same study directory. Read complete relevant theorem
sources and corrections before asserting updated rates, architecture coverage,
or activation scope. The communications task has not independently reviewed
those proofs. Report internal checking accurately; do not call it publication,
promotion, or external validation. Do not launch proof work or experiments.

Distinguish fixed-width, fixed-depth, finite-horizon accuracy from width-uniform,
depth-uniform, all-time, and practical-efficiency claims. Keep old/new clocks,
population moments/scalar aggregates, theory/implementation/experiments separate.
The README currently reports the new deep response-clock construction as not
implemented or tested. Retaining a dense initialization still costs storage and
matrix actions; moment storage also depends on sample count. These qualifications
should be precise in a technical note without overwhelming a friendly email.

## Relationships and actual status from the conversation

- **Francesco Orabona:** former colleague; the initial research message was
  already sent. Do not draft it as a new first contact or send it again.
- **Francis Bach:** my PhD co-advisor.
- **Thomas Hofmann:** I work in his group; I have now discussed the work at
  length with him. Date, specific feedback and agreed actions were not supplied.
- **Lorenzo Noci:** I am very close to him; first circle. I reported just
  messaging him on 2026-09-25; text, attachments and replies were not supplied.
- **Aurélien Lucchi:** first circle.
- **Antonio Orvieto:** I have already chatted with him. Topic, date and outcome
  were not specified; do not infer that he reviewed this study.
- **Vincent Fortuin:** friend.
- **Francesco Locatello:** former labmate; distinct from Orabona.
- **Fanny Yang and Niao He:** I have been close with them at various points.
- **Lénaïc Chizat and Blake Bordelon:** I know them.
- **Andrew Saxe:** I think I have a good connection with him.
- **Mehrdad Farajtabar:** I know him and we are coauthors. I also know several
  other Apple researchers through our plasticity paper; individual closeness
  was not specified for each coauthor.
- **Andrea Montanari:** I explicitly want to include him in outreach.
- **Boris Hanin:** I explicitly liked this suggestion; no direct relationship
  has been confirmed.

My ICLR 2026 paper is *Barriers for Learning in an Evolving World: Mathematical
Understanding of Loss of Plasticity*. Coauthors are Giulia Lanzillotta, Mohammad
Samragh Razlighi, Iman Mirzadeh, Keivan Alizadeh, Thomas Hofmann, Mehrdad Farajtabar,
and Fartash Faghri. Official links are in COMMS.md. It provides a natural shared
context for a message to those collaborators, but the closure is not already
proved to solve or explain plasticity loss.

Confirmed outreach now includes the Orabona and Lorenzo messages and the
conversations with Antonio and Thomas. The latest “just messaged Orabona”
report updates the existing event; it does not establish a second message.
Other emails, introductions, calls and seminars remain drafts or suggestions.
No assistant has sent anything.

## Most useful introduction routes to consider

- Lorenzo or Blake → **Boris Hanin**: documented coauthors; prefer one route.
- Antonio → **Albert Gu**: documented LRU coauthors; shorter than the older
  Mehrdad → Razvan Pascanu → Albert suggestion.
- Mehrdad → **Emmanuel Abbé** and **Samy Bengio**: documented coauthors.
- Ask Apple collaborators whether they know **Etai Littwin**: strong scientific
  fit, but an introduction route to him has not been verified.
- Francis → **Nicolas Flammarion** and possibly **Song Mei**; evidence in COMMS.
- Blake → **Cengiz Pehlevan**; Francis or Chizat may know **Eric Vanden-Eijnden**.

The EPFL list also includes Zdeborová, Krzakala, Hongler, Jaggi, and Cevher.
Additional reserve options are documented in COMMS.md. Coauthorship and shared
institutions support asking about an introduction; they do not prove closeness
or willingness. Browse current primary sources for new profile/connection claims
and preserve the sources in the record.

## What to do first

1. Reconcile COMMS.md with the current README for messaging, without taking
   over the scientific investigation or silently rewriting historical emails.
2. Propose a small next wave (roughly 3–5 people) with a distinct scientific
   question for each. The current unsent wave is Mehrdad, Francis and
   Aurélien, with Chizat as an alternative. Lorenzo is now a follow-up contact;
   account for his and Orabona's sent messages and the discussions with Thomas
   and Antonio before suggesting further outreach.
3. Draft the most useful unsent messages and introduction requests, using the
   shared plasticity work for Apple collaborators. Make clear which are ready
   to send and which require an attachment or a current theorem check.
4. Outline a reusable two-page research brief: construction, exact theorem,
   representative accuracy-versus-cost evidence, limits, and related work.
   No such brief or new figure was created in the earlier communications task.
   Keep the outline and drafts in COMMS.md initially; additional deliverables
   can follow my subsequent instructions.
5. Keep a factual contact log with dates, material shared, replies, and agreed
   next actions. Do not infer that a prepared draft was sent. Suggest follow-up
   timing without creating reminders or sending anything automatically.

Do useful preparation autonomously. Ask concise questions only when a missing
relationship detail or preference materially changes the next step. **Do not
send emails/messages, contact people, publish material, or create automations
without my explicit instruction for that action.**
