# Speaking notes

## Organization

Use Patrick Winston's [MIT lecturing heuristics](https://courses.csail.mit.edu/6.141/spring2010/pub/debates/Talk/phw.html) as delivery guidance. The recommendations here apply his principles to this talk, rather than attributing this exact sequence or wording to him.

Give an opening promise, develop one worked example, separate ideas that can be confused, state transitions, ask two answerable questions, and close on contributions. The revised order completes the quantum construction before the shorter adjacent-applications discussion. A topic footer supplies orientation without a separate transition slide.

## Opening and transitions

Opening, over the title:

> By the end, you will be able to follow an eight-bit error-correcting encoder and see how the same Boolean functions let us calculate a quantum gate.

Introduce memory as the application. Explicitly call the eight-bit construction a teaching example. Explain what the encoder and decoder know before showing a damaged table. The practical assumption is at most one bit flip at an unknown position.

After slide 7:

> We have recovered the message and proved the guarantee. Next, we will use these same eight-entry functions to specify a quantum encoding.

After slide 12:

> The eight-qubit calculation implements the desired gate, but this code cannot correct every one-qubit error. The next construction adds that protection.

After slide 17:

> That completes the quantum construction. The classical example also lets us discuss how much information a finite code can store, what happens on a probabilistic channel, and how predictable a Boolean output can be.

After slide 20, return to the contribution slide. Repeat the concrete construction and the test that proves its gate action. Leave those results visible during questions.

## Recurring example and conceptual distinctions

Point to the same address order whenever a table returns. On a cube, distinguish the address printed below a circle from the value or operation inside it. Read one endpoint calculation aloud before using a whole collection of edges.

- Four message bits specify the function. Three address bits index its eight values. Eight stored bits are its evaluation word.
- A corrupted table entry and a toggled function input are different operations. The Boolean derivative compares outputs at neighboring inputs. A corrupted entry changes one comparison in each fixed direction.
- Algebraic degree counts variables in a monomial. It does not count damaged entries and does not determine approximation by parity.
- XOR is binary addition. Weights, signed weights, and phase exponents use ordinary integer arithmetic.
- Classical codewords become physical basis words. Logical basis states are superpositions of several such words. Checking a phase on one representative does not check the entire encoded state.
- Site geometry determines coordinate evaluation words. Logical functions and rotation signs complete the quantum construction.
- A finite distance guarantee covers every error pattern up to a specified size. Channel capacity concerns a growing sequence of codes under a probabilistic noise model and specified decoding.
- Input-coordinate relabeling transports whole truth tables. Translating syndrome entries changes check data. The backup rank example illustrates this distinction, not an equivalence claim.

Avoid extra terminology when an existing object is enough. Say “affine function,” “codeword,” “parity,” or “encoded state” according to the object being discussed. A formula's first appearance should follow its domains and one concrete example. Notes expand definitions already visible in the slides.

## Audience pauses and reveals

On slide 6, first show the derivative and four votes. Ask:

> Why is this majority reliable?

Wait about seven seconds before revealing the coefficients and the constant. The supporting explanation is that the four edges are disjoint, so one changed endpoint can spoil only one comparison.

On slide 12, show the signed counts without the phases. Ask:

> Do +4 and −4 give different phases when each count contributes an angle of π/4?

Wait about seven seconds. Reveal that both phases are minus one. Connect the answer immediately to the requirement of equal phase within each encoded pair.

Six frames contain reveals: slides 6, 7, 12, 19, and 20 have two states, and slide 16 has three. The initial capacity state ends at the probabilistic model and definition of capacity. The initial Fourier state counts actual agreements before introducing signs. The overlap frame shows individual rows, then pairs, then triples in stationary positions.

Do not read concealed results aloud prematurely. Both audience pauses are included in the timing, not added after the 45-minute budget.

## Pacing

| Checkpoint | Target |
| --- | ---: |
| Classical code and distance finished, slide 7 | 14:00 |
| Eight-qubit gate checked, slide 12 | 23:30 |
| 48-qubit result stated, slide 17 | 34:00 |
| Further applications finished, slide 20 | 43:00 |
| Contributions finished, slide 21 | 45:00 |

Use literal transitions to let listeners rejoin. If behind time, shorten optional commentary or a second explanation of an established count. Keep the visible definitions, equal-phase argument, and decoder assumptions. The backup calculations are for questions, not part of the 45 minutes.

The abstract's computation promise is represented by the AND/XOR polynomial and input-toggle derivative. Communication is represented by explicit recovery, distance, packing, and erasure capacity. Cryptography is represented by the cubic function's affine predictability. The principal research result and the final contribution slide retain the quantum-error-correction emphasis.

## Human acceptance still needed

The build and finite calculations cannot establish whether the audience can follow the pacing. Rehearse with a mathematically mature listener outside QEC and ask for explanations in the listener's own words:

1. Which bits are message coefficients, which label positions, and which are stored?
2. Why do four disjoint comparisons recover a coefficient after one error?
3. Why must both physical words of an encoded pair receive the same phase?
4. Why do the 48-site weights become 24 and 32?
5. What changes between the fixed eight-bit guarantee and asymptotic capacity?

Record the time at the five checkpoints. If a definition has to be supplied orally to repair a missing step, revise the visible slide before calling the talk ready for this audience.
