# Applying Patrick Winston's How to Speak to this presentation

## Assessment

The strongest improvement is to make the audience anticipate, perform, and then recognize one calculation. Counting agreement first recovers a classical message, then exposes an affine predictor of the same Boolean table; signed counts later verify a logical quantum gate. The advertised computation, communication, and cryptography connections fit this story without introducing separate case studies.

Sources read: Winston's MIT OpenCourseWare [How to Speak lecture](https://ocw.mit.edu/courses/res-tll-005-how-to-speak-january-iap-2018/resources/how-to-speak-1/), its [full transcript](https://ocw.mit.edu/courses/15-371-innovation-teams-fall-2024/Unzc731iCUY_transcript.pdf), and his MIT-hosted [Lecturing Heuristics](https://courses.csail.mit.edu/6.141/spring2010/pub/debates/Talk/phw.html). The recommendations below apply those principles to this particular talk; they are not quotations or a claim that Winston prescribed this slide sequence.

## One idea, with clear boundaries

Winston recommends a central concept and repeated landmarks. His fences distinguish ideas that might be confused; verbal punctuation marks places where listeners can rejoin the argument. [Lecturing Heuristics](https://courses.csail.mit.edu/6.141/spring2010/pub/debates/Talk/phw.html), [transcript, p. 2](https://ocw.mit.edu/courses/15-371-innovation-teams-fall-2024/Unzc731iCUY_transcript.pdf#page=2)

For this presentation, the single idea is: **the same Boolean structure that helps recover a message can expose a predictable output—and can be deliberately chosen to implement a quantum gate.** The methods answer successive questions about one example; ANF, derivatives, Fourier analysis, and coding theory do not each need their own independent lecture. Hyperplanes clarify the same count on slides 6 and 16 without adding a geometry chapter.

The implemented chapters are:

| Chapter | Slides | Entry and exit |
| --- | --- | --- |
| Recover a message | 1–6 | Start with a corrupted table; end with the recovered coefficients and a proof of protection. |
| Understand a rule | 7–9 | Ask what changes or predicts the same rule; end with the distinction between high degree and weak affine predictability. |
| Control a gate | 10–20 | Turn measured structure into prescribed counts; end with the paper's code, exact test, and lower bound. |

The opening slide previews these three chapters. A footer identifies the current chapter. The title and closing slide repeat the same recovery/prediction/gate connection. The twenty-slide main talk retains its 45-minute budget, including audience pauses: 15 minutes through slide 6, 23.5 through slide 9, 26 through slide 10, 43.5 through slide 19, and 45 through slide 20.

Use three precise conceptual boundaries while speaking:

- **Input observation, input toggling, and channel corruption:** slide 7's derivative measures response to toggling a circuit input; decoding corrects a changed truth-table entry. Observing an input is a third operation.
- **Degree and affine predictability:** slide 9's cubic table still agrees with parity on 7/8 of uniform inputs. The ANF degree alone does not measure approximation quality.
- **Physical and logical operations:** slides 12–14 require all physical words in an encoded pair to receive the same phase. A pattern that works on one representative alone is insufficient.

Keep the first chapter closed after its decoder succeeds. The Fourier score revisits that success to reveal a shared notion of agreement; avoid starting another decoding tutorial. The quantum chapter then reuses counts rather than demanding that the audience learn another spectral theorem.

## Five priorities

### 1. Promise a specific ability before introducing notation

Winston recommends an opening promise about what the audience will understand or be able to do. [Transcript, pp. 1–2](https://ocw.mit.edu/courses/15-371-innovation-teams-fall-2024/Unzc731iCUY_transcript.pdf#page=1)

Approved opening, over the title and then the corrupted cube:

> By the end of this talk, you will follow one counting argument from repairing a corrupted message to controlling a quantum gate—and see why the same predictable structure matters in cryptography.

Immediately show the damaged table. State that the original rule was an XOR of selected inputs, possibly plus a constant. The audience now has a task and the exact promise needed to solve it. Preview the 48-qubit result in one spoken sentence, then earn the explanation through the toy example.

**Already reflected in the deck:** the opening recovery challenge and a complete route to the gate. **Proposed for delivery:** rehearse the promise and the brief research preview; the title text alone does not convey the whole promise.

### 2. Make one image and one surprise carry the talk

Winston associates memorable work with a symbol, a short phrase, a surprise, a distinctive idea, and a story. [Transcript, pp. 12–13](https://ocw.mit.edu/courses/15-371-innovation-teams-fall-2024/Unzc731iCUY_transcript.pdf#page=12)

For this talk, use the cube as the symbol. The surprise is specific: a useful agreement count for a receiver also exposes an unwanted predictor, and a signed distance calculation becomes a quantum-gate verification. A second slogan is unnecessary; repeat the opening's recovery/prediction/gate connection.

Repeat the connection at these landmarks:

- Slides 6 and 9: structure makes a message recoverable, while agreement with a simple rule can be undesirable in cryptography.
- Slide 14: distance to the same parity word determines exactly which encoded state gets a minus sign.
- Slide 16: whole-space weight minus deleted-subspace weight reuses the half-space count that established classical distance.
- Slide 20: the paper turns weight and overlap constraints into a construction and a lower bound.

**Already reflected in the deck:** the cube returns as the physical gate pattern; one Fourier slide serves both communication and prediction; the final slide states research contributions. **Proposed for delivery:** make the recurrence explicit rather than expecting the audience to notice it unaided.

### 3. Give the audience two calculations to finish

Winston recommends questions of manageable difficulty and allowing roughly seven seconds for an answer. [Transcript, pp. 2–3](https://ocw.mit.edu/courses/15-371-innovation-teams-fall-2024/Unzc731iCUY_transcript.pdf#page=2)

On slide 5, show the affine family and four edge votes, with the recovered coefficients and explanation concealed. Ask: “Why is this majority reliable?” Allow roughly seven seconds, then reveal the complete recovery. If needed, prompt orally that one corrupted endpoint belongs to just one of the four disjoint edges in that direction.

On slide 14, show signed weights 0, −4, and +4 without the phase column's answers. Ask: “Do +4 and −4 give different phases when each count contributes an angle of π/4?” Allow roughly seven seconds before revealing both phases as −1. The answer resolves why both strings in the encoded pair remain together.

**Implemented:** exactly four main frames have overlays: slides 5, 6, and 14 have two states each; slide 18 has three. Concealed elements reserve space. Slide 6 separates the four-point hyperplane from the distance consequence; slide 18 introduces rows, pairs, and triples in sequence. The deck has 20 numbered main slides, 15 backups, and 41 PDF pages including the title and reveals. Both audience pauses are part of the original slide times, not additions to the 45-minute budget.

### 4. Spend time on the mechanism; reduce simultaneous reading

Winston favors sparse slides, readable graphics, and a pace that permits absorption; board work can help establish that pace. [Transcript, pp. 4–8](https://ocw.mit.edu/courses/15-371-innovation-teams-fall-2024/Unzc731iCUY_transcript.pdf#page=4)

The highest-risk moments in this deck are slide 3's polynomial expansion, slide 8's Fourier score, and slide 18's congruences. Avoid reading any of those displays top to bottom without a visual referent.

- On slide 3, point to the one flipped entry before expanding its indicator; explain the cancellation of the three linear terms orally.
- On slide 8, compare the received bits with parity before reading the sum: seven agreements contribute +1 and one disagreement contributes −1. Identify that count with the plotted peak.
- On slide 18, reveal one congruence at a time in its reserved position. Relate the row condition to coefficient 1, recall slide 10's pair correction of −2, then explain the triple correction of +4. Reveal the logical-triple conclusion with the third state; explain orally why all higher terms vanish modulo eight.

**Implemented:** slide 6 marks the four parity-one vertices individually; slide 10 shows two coordinate faces and their shared edge; slide 16 subtracts the deleted subspace's weight from 32. Slide 17 separates sites, logical labels, and rotation signs. Slide 19 shows polynomial restrictions, geometric reductions, and logical-label tests. The full inclusion–exclusion formula and degree/rate table remain in backup; Fourier analysis still uses only one score and one spectrum. **Pending delivery check:** test legibility from the back of the actual room and rehearse the pauses. Optional board work must fit the allocated time.

### 5. End with what the paper accomplished; rehearse with newcomers

Winston recommends leaving contributions visible during questions and practicing with people unfamiliar with the research. [Transcript, pp. 10 and 13–14](https://ocw.mit.edu/courses/15-371-innovation-teams-fall-2024/Unzc731iCUY_transcript.pdf#page=10)

**Already changed:** slide 20 now presents the 48-qubit construction, the exact signed-weight test, and the conditional lower bound. Keep that slide displayed during questions rather than advancing into the backups automatically.

Suggested last substantive sentence:

> The same Boolean structure can help recover a message, expose a predictable output, and be deliberately chosen to control a protected quantum gate.

**Human rehearsal still required:** ask a mathematically mature listener outside QEC to explain, without looking at the slides, why a hyperplane gives weight four, why the 48-site construction gives weights 24 and 32, and why equal phase within an encoded pair matters. Also check whether the listener can distinguish agreement's usefulness in decoding from its undesirability in cryptographic prediction. Record the chapter completion times and the total duration, including both audience pauses. The 45-minute allocation remains an estimate until rehearsal; compilation and finite checks do not establish audience comprehension.

## What to adapt rather than follow mechanically

Winston's five-minute vision/accomplishment advice is directed at job talks. A brief early preview suits this seminar; moving the whole QEC section forward would conflict with the intended fundamentals-first structure. The source's numerical font suggestions should be translated into an actual projection test, since Beamer page sizes differ from conventional slide software. A forced joke, artificial mannerism, or rigid rule about the final courtesy would add little here.

Affine equivalence should remain in backup. The classification topic supplies a useful answer to a symmetry question, but introduces a new matrix action and a second equivalence convention before the main promise has been fulfilled. A short spoken observation that cube relabeling preserves the code is sufficient unless that question arises.

The two added backups clarify limits rather than creating new main topics. Translating a four-point face preserves affine dimension but can change syndrome rank; transporting all physical code data under a position permutation is a different operation. A polynomial factor can confine support to a hyperplane, but the reduction depends on the origin case and the paper's code hypotheses. A zero syndrome column need not be a zero full generator column. Keep classification tables, polar matrices, orbit enumeration, and full-support puncturing in the tutorials.
