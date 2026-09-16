# Speaking notes

## Organization

Use Patrick Winston's [MIT lecturing heuristics](https://courses.csail.mit.edu/6.141/spring2010/pub/debates/Talk/phw.html) as delivery guidance. Give a concrete opening promise, finish one worked example, separate quantities that can be confused, use explicit transitions, ask two answerable questions, and close on the author's contributions.

The classical encoder and its eight addresses remain the reference point throughout the talk. Complete the classical calculation before introducing quantum states. Complete the 48-qubit construction before discussing adjacent applications. A footer marks the three portions without adding transition slides.

## Opening and transitions

Over the title, say:

> By the end, you will be able to follow an eight-bit error-correcting encoder and see how the same Boolean functions let us calculate a quantum gate.

Introduce computer memory as the practical setting. Call the eight-bit construction a teaching example. State what the encoder, memory readout, and decoder each contain before showing a corrupted table.

After slide 9, say:

> We have specified the encoder, corrected its readout, and proved why the correction is unique. Next, the same eight affine tables will become physical basis words in a quantum encoding.

After slide 13, say:

> The eight-qubit calculation implements the desired gate, but this encoding does not correct every one-qubit error. The 48-qubit construction keeps the phase calculation and adds that protection.

After slide 17, say:

> That completes the quantum construction. I will use the classical example once more to discuss finite code bounds, probabilistic erasures, and prediction of a Boolean output.

After slide 20, return to the contribution slide. State the construction and its phase test. Leave those results visible during questions.

## Classical example

On slide 1, explain a memory write and read. The encoder computes eight stored values from four message bits. The decoder uses constraints among those values. At most one value changes, and the decoder does not know its address.

On slide 2, read the XOR table aloud before using the symbol. Distinguish the message coefficients from the address bits. Calculate the value at address `101` in front of the audience. Explain that redundancy creates alternative representations of the same 16 messages. It does not create new message information.

On slide 3, use the displayed recovery formulas to prove that no two messages share an uncorrupted word. Only then call the 16 outputs codewords. “Affine Boolean function” is the standard name for the constant plus binary linear terms in the encoder.

On slide 4, point first to the two eight-bit words. Define `r` as the table read from memory. Define the indicator by its two evaluation cases before expanding it. Degree describes the largest monomial in the ANF. Degree does not count corrupted positions.

On slide 5, read the `000,100` comparison aloud. The derivative toggles an input coordinate and compares two output values. Corrupting a stored value is a different operation. One changed endpoint alters one of the four disjoint comparisons in every fixed coordinate direction.

On slide 6, show the four votes and ask:

> Why is this majority reliable?

Wait about seven seconds. Reveal that a changed address belongs to only one of the four disjoint edges. Recover all three linear coefficients, subtract their affine contribution by XOR, and recover the constant from the seven equal residual entries.

On slide 7, define support, weight, and Hamming distance in that order. Use the colored coordinate faces to count four points in each support and two in their intersection. The calculation `4+4-2(2)=4` is the Hamming distance of one particular pair of evaluation words.

On slide 8, define the minimum distance of the code as a minimum over every distinct codeword pair. Pair vertices to prove the four-or-eight alternative. Explain the hyperplane terms only after the parity level sets are visible. On the reveal, read the contradiction from left to right. The proof shows that one readout cannot be within one bit of two different codewords.

On slide 9, pause on the two displayed distances:

- `d_H(p,r)=1` describes the displayed codeword and damaged readout.
- `d_min(C)=4` describes the smallest separation anywhere in the classical code.
- `d_Q`, introduced later, measures support of an undetected logical quantum error.

Do not call `d_H(p,r)` the code distance.

## Quantum construction

On slide 10, define each basis vector before using kets elsewhere. A bit flip exchanges basis vectors. A phase flip changes the sign between components of a superposition. Explain that a diagonal operation leaves a basis label unchanged while multiplying it by a complex phase.

On slide 11, connect every complementary word to the affine encoder. The all-site bit flip exchanges the two terms in a pair, so the normalized sum is fixed. A diagonal physical operation preserves the encoded state only when both words receive the same phase.

On slide 12, count an explicit word before reading the signed-weight formula. Keep XOR arithmetic separate from the ordinary integer sum used in the signed count.

On slide 13, show signed counts without the phase answers and ask:

> Do +4 and −4 give different phases when each count contributes an angle of π/4?

Wait about seven seconds. Reveal that both give minus one. Point out that the calculation checks every word in each encoded state.

On slide 14, define the six-bit address as the pair `(u,w)`. The full space contains 64 addresses. Deleting `w=00` removes 16. Apply the earlier half-space pairing argument to the full linear function and again to its restriction. The two cases give 24 and 32.

On slide 15, introduce the six coordinate evaluation words before the span `S`. Flipping the support of one coordinate word permutes the 64 terms in each encoded state. Define this fixed operation as a stabilizer check. Then define the logical functions, labels, signs, and encoded superposition. The geometry does not determine the logical functions or signs by itself.

On slide 16, define a generator row and coordinatewise multiplication. Explain that each product marks a support intersection. The three reveal states follow the integer coefficients `1`, `−2`, and `4`. Terms from four or more rows have coefficients divisible by eight. The logical triple is the sole odd triple and produces the logical CCZ phase.

On slide 17, define quantum distance before giving `d_Q=3` and `[[48,3,3]]`. Distance three means the code corrects an arbitrary error supported on one physical qubit. Keep this quantity distinct from the classical `d_min(C)`.

## Adjacent applications

On slide 18, name `RM(1,3)` only after the audience has already constructed it. Define `[n,k,d_min]` through stored bits, message bits, and classical minimum distance. Explain all factors in `16(1+8)=144≤256` before naming the Hamming bound.

On slide 19, define a known-location erasure and inspect both finite examples. Then define the probabilistic model and asymptotic capacity. Reveal the Reed–Muller theorem only after those definitions. State that the theorem concerns a growing sequence and optimal block decoding. It does not describe the finite majority decoder from slide 6.

On slide 20, count seven agreements before introducing real signs. Agreements contribute plus one and the disagreement contributes minus one, giving `3/4`. Accurate affine prediction is undesirable for a cryptographic Boolean component. The example also separates algebraic degree from affine predictability.

## Concepts that must remain distinct

- Four message bits specify an affine function. Three address bits select one of its eight values.
- A stored-bit error changes a table entry. A Boolean derivative changes an input coordinate and compares outputs.
- XOR is binary addition. Weight, signed weight, and phase exponents use ordinary integer arithmetic.
- `d_H(f,g)` compares one pair of words. `d_min(C)` minimizes over a classical code. `d_Q` measures the support of an undetected logical quantum error.
- A physical basis word is one binary string. An encoded basis state is a superposition of many physical basis words.
- A finite distance guarantee is a worst-case statement at fixed length. Capacity is an asymptotic statement for a probabilistic channel and a specified decoder.

## Reveals and pacing

Slides 6, 8, 13, 19, and 20 have two states. Slide 16 has three. Do not read a concealed conclusion before advancing. The common parts of every slide remain stationary.

| Checkpoint | Target |
| --- | ---: |
| Decoder complete, slide 6 | 12:00 |
| Classical recap complete, slide 9 | 18:00 |
| Eight-qubit gate complete, slide 13 | 26:00 |
| 48-qubit result complete, slide 17 | 34:00 |
| Adjacent applications complete, slide 20 | 43:00 |
| Contributions complete, slide 21 | 45:00 |

If time is short, reduce repeated explanation after a calculation. Keep every visible definition, the decoder assumptions, the equal-phase argument, and the distinction among the three distances.

## Human acceptance still needed

Rehearse with a mathematically mature listener outside quantum error correction. Ask the listener to explain:

1. Which bits are message coefficients, which bits label positions, and which bits are stored.
2. Why four disjoint comparisons recover a coefficient after one error.
3. Why `d_H(p,r)=1` and `d_min(C)=4` are compatible.
4. Why both physical words in one encoded pair need the same phase.
5. Why the 48-site counts are 24 and 32.
6. Why a fixed finite-distance guarantee differs from channel capacity.

Measure the six timing checkpoints. If a definition must be supplied orally before a listener can parse the visible slide, revise the slide.
