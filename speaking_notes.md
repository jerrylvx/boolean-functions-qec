# Speaking notes

Use the [one-page cue card](speaking_card.pdf) beside you; the detailed notes below provide the full narration context.

## Delivery contract

The slide supports the spoken explanation. Definitions can be spoken before the audience needs them; symbol roles and assumptions essential for reading an equation remain visible. Keep one example or calculation at the center of attention. Avoid reading paragraphs verbatim.

Follow [Patrick Winston’s lecturing heuristics](https://courses.csail.mit.edu/6.141/spring2010/pub/debates/Talk/phw.html): promise a concrete understanding, revisit the central example, mark transitions, ask answerable questions, and finish with the author’s contributions. The two seven-second pauses occur on slides 6 and 15.

## Slide-by-slide cues

### Title. Title (00:00–00:30)

**Already established:** No Boolean-function, coding-theory, or QEC background assumed.

**Terms and symbols now:** None

**Point and explain:** Promise: We will construct a small error-correcting code, then use the same Boolean-function calculations to understand a quantum gate. Basic arithmetic is sufficient to start; explain the quantum vector notation when it arrives.

**Advance:** One title page. Keep the promise spoken; do not restore the deleted title-page roadmap.

**Say next:** Begin with writing a message into memory.

### 1. Correcting one bit of error in memory (00:30–01:30)

**Already established:** Bits and ordinary counting.

**Terms and symbols now:** Encoder, decoder, message, readout

**Point and explain:** Point from four message bits to eight stored values and then to the changed value. The decoder knows the encoder but not the changed position. Extra stored values create constraints without adding message information. Say that this is a teaching encoder motivated by error-correcting memory, not the design of a particular device.

**Advance:** One state. State the at-most-one-error assumption before claiming correction.

**Say next:** We must specify how each of those eight bits is computed.

### 2. The encoder evaluates eight XOR expressions (01:30–04:00)

**Already established:** Message versus stored word.

**Terms and symbols now:** XOR ⊕; message b,a₁,a₂,a₃; a=(a₁,a₂,a₃); address u=(u₁,u₂,u₃); fₐ,ᵦ

**Point and explain:** Read the four XOR outcomes; products of bits mean AND. Message coefficients remain fixed while the address runs through eight positions. Point to column 101: b XOR a₁ XOR a₃ gives 0 XOR 1 XOR 1 = 0. The general expressions specify all sixteen messages, not just the displayed example.

**Advance:** State 1: message/address roles, formula, and expression rows. Compute column 101 aloud. State 2: reveal all example values and the complete stored word.

**Say next:** This encoder has a familiar mathematical description.

### 3. Affine Boolean functions define the codewords (04:00–05:30)

**Already established:** The encoder formula and address order.

**Terms and symbols now:** Boolean function; affine; e₁=100,e₂=010,e₃=001; codeword; C

**Point and explain:** A Boolean function is the complete input-output table. An affine function is a constant XOR selected input bits. Introduce eᵢ before the recovery formula. The value at zero gives b; comparing zero with eᵢ gives aᵢ. Therefore no two messages encode to the same word. The receiver knows this family because it knows the encoder.

**Advance:** One state. Read definitions, then demonstrate the recovery formulas, then infer sixteen distinct codewords.

**Say next:** Now inspect the actual readout as a function too.

### 4. From a truth table to a polynomial (05:30–07:30)

**Already established:** The affine encoder and the single changed entry.

**Terms and symbols now:** p: parity; r: readout; algebraic normal form (ANF); degree

**Point and explain:** Point first to p and r. At 000 every factor of (1 XOR u₁)(1 XOR u₂)(1 XOR u₃) is one; elsewhere some factor vanishes. Expanding cancels parity’s linear terms. ANF is a description of the damaged table, not a step the decoder must perform. Degree counts variables in the largest product term, not errors.

**Advance:** State 1: original and corrupted words. State 2: construct the indicator product. State 3: name ANF, expand, and compare degree with the code family.

**Say next:** To decode, compare neighboring table entries.

### 5. Comparing neighboring table entries (07:30–09:30)

**Already established:** Addresses, parity, and the readout.

**Terms and symbols now:** Direction eᵢ; Boolean derivative Dₑᵢf

**Point and explain:** Read the values at 000 and 100 before the derivative formula. Changing an input address is not corrupting a stored output. The changed entry belongs to one disjoint edge in each fixed direction; the other three comparisons remain intact. The derivative is 1 when moving along that edge changes the output.

**Advance:** State 1: cube and the explicit endpoint comparison. State 2: derivative formula and four-edge table.

**Say next:** For an affine function, every comparison in one direction should give the same coefficient.

### 6. Recovering the four message coefficients (09:30–11:30)

**Already established:** Four disjoint comparisons in each direction.

**Terms and symbols now:** Reuse Dₑᵢf, aᵢ, b; majority; residual values

**Point and explain:** Toggling uᵢ cancels terms independent of uᵢ. Ask: Why is this majority reliable? Wait seven seconds. One changed address can spoil only one vote, leaving at least three correct votes. All three directions work the same way. After recovering a, XOR its contribution out of every readout entry; at least seven residuals equal b.

**Advance:** State 1: derivative identity and votes, with the question. State 2: majority argument, coefficients, residual word, and constant. Do not give the explanation before the pause.

**Say next:** We have a decoder. Now explain why no other allowed message can fit the same corrupted readout.

### 7. Intersections count differing positions (11:30–13:15)

**Already established:** Products mean AND; XOR indicates disagreement.

**Terms and symbols now:** Support in words; wt(f); Hamming distance d_H(f,g)

**Point and explain:** The support is the positions with value one; weight counts them. Point to the two colored coordinate faces and common edge. Four plus four counts the intersection twice, whereas XOR excludes it. Subtract two copies of the two-point overlap. Weight arithmetic is ordinary integer arithmetic.

**Advance:** State 1: faces, counts, and overlap reasoning. State 2: general identity, definition of pairwise distance, and d_H(u₁,u₂)=4.

**Say next:** The same four-versus-four count holds for any nonconstant affine function.

### 8. Nonconstant affine functions have four ones (13:15–15:00)

**Already established:** Affine functions and four disjoint address pairs.

**Terms and symbols now:** Affine hyperplane; reuse p and eᵢ

**Point and explain:** Choose a coordinate with a nonzero coefficient. Its four pairs each contain exactly one one. Introduce the geometry only after the count: inputs giving a specified output form an affine hyperplane. Parity’s zero set is a linear hyperplane through zero; its one set is a translate. Do not draw a Euclidean plane through the four parity-one vertices.

**Advance:** State 1: paired cube and four ones. State 2: geometric name and parity-one addresses. Backup trigger: Does changing the binary coordinates change these counts or the code?

**Say next:** Apply this count to the difference between two allowed codewords.

### 9. Minimum distance makes correction unique (15:00–16:45)

**Already established:** Every nonconstant affine function has four ones.

**Terms and symbols now:** d_min(C), distinct from d_H(f,g)

**Point and explain:** The XOR of two distinct affine words is nonzero affine: four ones if nonconstant, eight if constant. The earlier coordinate pair attains four, so the minimum is exactly four. If two candidates were each within one change of r, joining those changes would put them within two of one another. This contradicts their minimum separation.

**Advance:** State 1: define and establish d_min(C)=4. State 2: two hypothetical candidates, the distance chain, and unique correction.

**Say next:** Review what is now fully established before changing physical setting.

### 10. What the classical example established (16:45–18:00)

**Already established:** Completed classical example.

**Terms and symbols now:** No new terms; d_H(p,r)=1 and d_min(C)=4

**Point and explain:** Point through affine evaluation, polynomial description, derivative recovery, and unique correction. The observed one-bit corruption is a distance between one word and one readout. The minimum distance belongs to the entire code. Neither statement replaces the other.

**Advance:** One state; this is a recap, not another proof.

**Say next:** The sixteen classical words form eight complementary pairs. Each pair will represent one quantum basis state.

### 11. A quantum state has amplitudes and relative phase (18:00–19:30)

**Already established:** Vectors can be described by coordinates; define the notation here.

**Terms and symbols now:** Qubit; basis vectors |0⟩,|1⟩; amplitude; superposition; relative phase; bit and phase flip

**Point and explain:** Read the two basis vectors before using their kets in a sum. Amplitudes are complex coefficients whose squared magnitudes sum to one. The equal sum is normalized by 1/√2. A phase flip changes the relative sign of its two components; multiplying both by the same unit complex factor does not change the physical state. A bit flip exchanges the two basis vectors.

**Advance:** State 1: basis and normalized superposition. State 2: relative versus overall sign; then bit flip.

**Say next:** The physical operation in the construction rotates one amplitude by a fixed angle.

### 12. Single-qubit rotations add phase angles (19:30–21:00)

**Already established:** Amplitudes and relative phase.

**Terms and symbols now:** T,T†; eⁱθ; physical basis word |v⟩

**Point and explain:** The circle represents a unit complex multiplier, not a Bloch sphere. Introduce i and the angle notation. T fixes |0⟩ and multiplies the |1⟩ amplitude by a forward π/4 phase; T† reverses it. A string inside a ket labels the physical bits. In 00101 there are two ones, so the two factors multiply and their angles add.

**Advance:** State 1: rotation arrows and the single-qubit action. State 2: explicit word and weight-to-phase formula.

**Say next:** We need these rotations to act correctly on an encoded superposition.

### 13. Complementary words encode three qubits (21:00–23:30)

**Already established:** Sixteen affine words; complementary constants; quantum superposition.

**Terms and symbols now:** Logical label a; encoded state |a⟩_L; physical versus logical qubits

**Point and explain:** Show a=000 first: the all-zero and all-one words form a normalized pair. Each of the eight labels has two distinct physical words, and no word is shared between pairs; this gives orthogonal states. Their arbitrary superpositions encode three logical qubits. The hardware uses eight physical qubits. For one encoded pair, unequal phases would change the ratio between its two amplitudes and take it outside the intended one-dimensional pair state.

**Advance:** State 1: complementary table and normalized pair. State 2: eight encoded states and equal-phase requirement. Orally compare a plus pair with a plus/minus pair using the preceding slide.

**Say next:** Specify the desired operation on the logical labels, then choose physical rotations.

### 14. Choosing rotations for a three-qubit sign change (23:30–25:00)

**Already established:** Logical labels and physical phase accumulation.

**Terms and symbols now:** CCZ; signed weight W(v)

**Point and explain:** State the desired change: only logical 111 gets a minus sign. Name controlled-controlled-Z afterward. The address determines the physical rotation once and for all. For the word p, its four ones are all at inverse rotations, giving signed count −4. W counts ones with signs; it does not count addresses with parity one independently of v.

**Advance:** State 1: logical target, rotation cube, and explicit count. State 2: signed-weight definition and physical phase.

**Say next:** Check both physical words at every logical label.

### 15. Checking every encoded pair (25:00–27:30)

**Already established:** Signed counting and the classical affine weight argument.

**Terms and symbols now:** Reuse W, p, fₐ,ᵦ, d_H

**Point and explain:** At parity-zero addresses, XOR with p leaves v; at parity-one addresses, subtracting p turns the contribution into −v. Summing gives W(v)=d_H(p,v)−4. If a differs from 111, the affine difference is nonconstant. At 111, the two words are parity and its complement. Ask whether +4 and −4 give different phases and wait seven seconds. Both phases are −1; equal phase within each pair and label dependence together establish CCZ.

**Advance:** State 1: identity and count table with phase cells blank. State 2: fixed-position phase entries and conclusion. The question/conclusion share a reserved area.

**Say next:** The gate calculation works. The next construction adds protection against an arbitrary one-qubit error.

### 16. Selecting 48 physical positions (27:30–28:15)

**Already established:** Physical positions index evaluation-word entries.

**Terms and symbols now:** u now has four bits; w has two bits; six-bit address (u,w)

**Point and explain:** Explicitly announce that u is now a four-bit within-block address; the previous cube used three bits. The two bits w label four blocks. Delete w=00 and retain three blocks of sixteen sites. The toy code’s limitation motivates a larger construction; geometry alone does not complete the code.

**Advance:** State 1: all four blocks. State 2: cross out the zero block and count 48. Backup trigger: Why does the eight-qubit code not already correct every one-qubit error?

**Say next:** Evaluate linear functions on the retained positions and count their ones.

### 17. The retained linear words have weights 24 and 32 (28:15–29:45)

**Already established:** The earlier affine pairing argument and the deleted block.

**Terms and symbols now:** Linear means XOR of selected bits without a constant; reuse wt

**Point and explain:** Every nonzero linear function on six bits has 32 ones. If a within-block bit occurs, its restriction to the deleted block is still nonzero linear, with eight ones. Otherwise a nonzero function of w is zero on the deleted block. Use u₁ and w₁ as examples of these exhaustive cases. The zero function gives weight zero. Divisibility of ordinary weights does not by itself prove the signed phase conditions.

**Advance:** State 1: the full-space count. State 2: u₁ and 32−8. State 3: w₁ and 32−0; distinguish ordinary from signed counts.

**Say next:** The six coordinate evaluation words generate the superpositions used by the code.

### 18. Summing stabilizer words gives an unchanged state (29:45–30:45)

**Already established:** Coordinate evaluation and quantum sums.

**Terms and symbols now:** S₁,…,S₆; S; stabilizer

**Point and explain:** The six coordinate words are independent: no nonzero linear combination vanishes on all retained sites, since its weight is 24 or 32. Thus six binary choices give 64 distinct words. Their equal-amplitude sum has normalization 1/8. A mask Sᵢ specifies physical bits to flip; it does not change the coordinate labels. Adding the same mask permutes the collection.

**Advance:** State 1: six words, their combinations, and normalized sum. State 2: paired summands and the stabilizer name. The next slide verifies the operation on every encoded label.

**Say next:** Choose different disjoint collections to store the eight logical labels.

### 19. Logical functions distinguish eight encoded states (30:45–31:45)

**Already established:** A normalized sum over 64 words and stabilizer permutations.

**Terms and symbols now:** K₁,K₂,K₃; K(a); reuse S and |a⟩_L

**Point and explain:** For a=100, shift every word by K₁. The logical functions are chosen so that the eight shifted collections are disjoint; this is a checked property of the construction, not a consequence of site geometry alone. Adding Sᵢ permutes each shifted collection, fixing every encoded state. Other phase-type checks are part of the completed code; the six displayed operations are not asserted to be its entire check set.

**Advance:** State 1: logical words and one translated collection. State 2: the general encoded-state formula and invariance. Backup trigger: What are the actual logical functions?

**Say next:** Now assign a physical rotation at every retained position.

### 20. Assigning the physical rotations (31:45–32:30)

**Already established:** The three blocks and encoded states.

**Terms and symbols now:** Reuse T,T†,W; fixed 48-site pattern

**Point and explain:** Point to the row and column order before reading a site. The block counts are 6,6,10 inverse rotations. W has the same meaning as before, but now uses this fixed 48-site pattern. The sign polynomial is optional detail; the visible pattern is the actual verified construction.

**Advance:** One state. Backup trigger: How is this rotation pattern specified?

**Say next:** We can verify all encoded phases using counts of row intersections.

### 21. XOR produces intersection terms (32:30–33:30)

**Already established:** Support intersection identity and the nine evaluation words.

**Terms and symbols now:** Generator row; g₁,g₂,g₃ as distinct selections; coordinatewise product

**Point and explain:** A generator row is simply one of the three logical words or six stabilizer words. Recall the two-face count before the three-row expression. These are integer identities: XOR has been expressed using ordinary plus, minus, and products. At a site shared by all three rows, the first two groups contribute 3−6; adding 4 restores the XOR value 1.

**Advance:** State 1: pair identity and recalled picture. State 2: three-row expansion and coefficients 1,−2,4.

**Say next:** Weight these integer contributions by the fixed physical rotation signs.

### 22. Signed intersections verify the logical gate (33:30–35:30)

**Already established:** Integer expansion and physical phase e^(iπW/4).

**Terms and symbols now:** Congruence modulo 8,4,2; reuse W and generator rows

**Point and explain:** Adding eight to W adds 2π to the angle. Thus only its remainder modulo eight matters. A row contribution must vanish modulo eight; a pair contribution is multiplied by −2, so divisibility by four suffices. A triple is multiplied by four, so only its parity matters. The logical triple is odd and all other triples even. Higher XOR-expansion coefficients are multiples of eight. The resulting W is independent of the selected stabilizer word, while its logical-label dependence is exactly 4a₁a₂a₃.

**Advance:** State 1: remainder explanation and row condition. State 2: pair condition. State 3: exact triple condition, higher-term explanation, and phase conclusion. Equations remain stationary.

**Say next:** This proves the gate for the displayed code and rotation pattern; state error protection separately.

### 23. The resulting quantum code (35:30–37:00)

**Already established:** Encoded information; bit/phase flips; stabilizers and completed phase test.

**Terms and symbols now:** Stabilizer check; d_Q; [[48,3,3]]

**Point and explain:** A check tests whether a stabilizer has its expected value. Quantum distance refers to the smallest support of an undetected nontrivial logical product of bit and phase flips. The paper establishes distance three using all code checks, so the code corrects an arbitrary one-site error. The signed-overlap calculation alone does not establish distance. The construction, distance proof, and exact gate criterion are distinct research results.

**Advance:** One state. Backup trigger: Is 48 the smallest possible length? Keep all restrictions in the backup answer.

**Say next:** That completes the quantum construction. The classical example also belongs to a much larger family of codes.

### 24. Reed–Muller codes and finite packing (37:00–39:00)

**Already established:** Classical affine code, polynomial degree, and unique correction.

**Terms and symbols now:** RM(d,m); linear code; [n,k,d_min]; Hamming bound

**Point and explain:** Name RM(1,3) only now. More generally evaluate all Boolean polynomials of degree at most d at every m-bit address. Closed under XOR means linear. Point to n=8 stored bits, k=4 message bits, and minimum distance four. Each center in the picture represents a codeword, and its eight neighbors represent single-bit changes. The circles are schematic sets, not Euclidean geometry. Count nine readouts for each of sixteen messages.

**Advance:** State 1: family and parameters. State 2: packing picture and 144≤256. Do not introduce the general binomial packing formula.

**Say next:** What changes when positions are known to be missing rather than silently flipped?

### 25. Recovering missing data and approaching capacity (39:00–40:45)

**Already established:** Finite classical error correction and Reed–Muller code family.

**Terms and symbols now:** Erasure; rate; capacity; no new mathematical symbols

**Point and explain:** Point to the question-mark cell. Its location is known, unlike our earlier bit error. Rate means information bits per transmitted bit. Capacity is an asymptotic benchmark for a specified random channel, not a guarantee for every finite loss pattern. For independent erasures, suitable growing Reed–Muller sequences achieve that benchmark under optimal whole-block decoding. No efficient-decoder claim is being made.

**Advance:** State 1: erasure picture and finite recovery. State 2: verbal definitions and qualified asymptotic result. Keep the exact theorem in the source note below.

**Say next:** The same functions can also be studied as computations whose outputs we want to predict.

### 26. Predicting outputs, learning, and cryptography (40:45–43:00)

**Already established:** The original p/r table and derivative comparisons.

**Terms and symbols now:** Fourier analysis; statistical learning; reuse parity and r

**Point and explain:** Read the seven agreements and one disagreement under equally likely inputs. Fourier analysis measures correlations with parity patterns; the statement is a verbal summary, with no transform formula to derive. Recall derivatives as a way to ask whether changing an input changes the output. Learning uses input-output examples to predict new outputs; appropriate function structure can make this possible. Do not imply arbitrary Boolean functions are efficiently learnable. Predictability can be useful for learning and undesirable for a cryptographic component. Degree three alone did not prevent this strong parity approximation.

**Advance:** State 1: agreement cells. State 2: Fourier interpretation. State 3: examples-to-predictions picture and learning/cryptographic implications.

**Say next:** The broader applications ask different questions about Boolean functions. My construction uses their evaluation words and intersection counts to control an encoded quantum gate.

### 27. Contributions (43:00–45:00)

**Already established:** The completed construction, gate calculation, and short applications overview.

**Terms and symbols now:** No new notation or claims

**Point and explain:** Repeat the three contributions: explicit protected encoding, the 26T+22T† implementation, and the exact phase criterion. Connect the opening weight count to the final intersection calculation. Leave the contributions visible throughout questions; use the backup links only when their questions arise.

**Advance:** One state. Backup trigger: Where can I read more?

**Say next:** Stop after the contributions; invite questions without adding a new topic.

## Backup use

| Primary anchor | Trigger | Backup answer and return |
|---|---|---|
| Slide 8, final state | Does changing the binary coordinates change these counts or the code? | Affine equivalence; return button restores slide 8, final state. |
| Slide 16, final state | Why does the eight-qubit code not already correct every one-qubit error? | Toy quantum distance; return button restores slide 16, final state. |
| Slide 19, final state | What are the three logical functions? | Explicit logical functions; return button restores slide 19, final state. |
| Slide 20, final state | How is this rotation pattern specified? | Rotation-sign polynomial; return button restores slide 20, final state. |
| Slide 23, final state | Is 48 the smallest possible length? | Qualified length exclusion; return button restores slide 23, final state. |
| Slide 27, final state | Where can I read more? | Sources; return button restores slide 27, final state. |

The toy-distance backup may be opened before stabilizers are taught in the main sequence, so it defines a check locally. Its two-site phase error changes relative phases between logical labels, not within a fixed complementary pair. The logical-function backup shows one block per reveal. The length backup retains CSS, three logical qubits, phase distance at least three, and the Campbell–Howard hypotheses; it makes no global-minimality claim.

## Exact source qualifications for the overview

**Memory.** [IBM, Troubleshooting Memory issues](https://www.ibm.com/support/pages/troubleshooting-memory-issues) provides the ECC-memory motivation. The eight-bit construction is pedagogical.

**Erasure capacity.** [Kudekar et al., Theorem 27](https://arxiv.org/pdf/1601.04689) gives a growing sequence of Reed–Muller codes whose rates converge to any fixed target in (0,1), achieving binary-erasure capacity under block-MAP decoding. For independent erasure probability ε and limiting rate R, whole-word error tends to zero when ε < 1−R. The channel capacity is 1−ε. These symbols are source-reference notes, not a new on-slide derivation. Optimal decoding does not imply that the finite majority decoder achieves this result or that a practical efficient decoder has been supplied.

**Boolean analysis and learning.** [O’Donnell, Chapters 1–3](https://arxiv.org/pdf/2105.10386) develops parity correlations, influences/derivatives, and learning under structural assumptions. Learning from examples requires assumptions on the function class and sampling model. Do not assert that arbitrary Boolean functions, or all functions described informally as having simple spectra, are efficiently learnable. The main slide only illustrates prediction and says suitable structure can help.

## Sequential cold-read review

This is an assistant’s linear review of the slides with intended narration, not an outside-listener test. Entries record where each explanation belongs.

| Slides | Potential obstacle | Treatment |
|---|---|---|
| Title, 1 | Why extra bits help; whether this is a real hardware design | Diagram and one-error assumption visible; teaching-example qualification spoken. |
| 2 | Message bits confused with address bits; formula before XOR | Distinct roles and XOR outcomes visible; work 101 before revealing example values. |
| 3 | Unexplained affine family or sixteen-word claim | Define the function; inverse recovery proves distinctness. No separate encoder-map symbol. |
| 4 | ANF seems to be required by decoder; degree mistaken for number of errors | Indicator before expansion; describe ANF’s role orally and distinguish the two counts. |
| 5 | Formula precedes its meaning; input changes confused with memory errors | Endpoint example first; derivative and other edges revealed afterward. |
| 6 | Constant recovery omitted; answer spoiled before pause | Votes first, then coefficients and residuals; reserved question/conclusion area. |
| 7 | Support and distance arrive as abstract notation | Large face picture; support defined verbally, weight and distance retained as reusable notation. |
| 8 | Hyperplane suggests a Euclidean plane through parity vertices | Show discrete paired vertices; introduce the name only after the count. |
| 9 | Pairwise distance confused with minimum; difference-function coefficient reuses aᵢ | Separate frame and quantities; describe f XOR g directly without a new coefficient family. |
| 10 | Classical calculation does not prepare the quantum transition | Recap completed results; explicitly sixteen words and eight pairs. |
| 11 | Kets, normalization, relative and overall phase appear together | Basis and normalized sum first; reveal sign comparison; spell out operational difference aloud. |
| 12 | Phase circle mistaken for a qubit-state sphere; word phase unmotivated | Say it depicts a complex multiplier; count ones in 00101 before generalizing. |
| 13 | Logical qubit used before encoding; equal-phase condition asserted | Construct a pair first; disjointness explains eight states; relate unequal phases to prior sign example. |
| 14 | CCZ and signed weight used before their purpose | Desired label sign first, then gate name; count parity’s four inverse sites before W. |
| 15 | A physical-word calculation does not establish logical action | Table checks both words of every pair; explain equal phase within pairs and different phases between labels. |
| 16 | u silently changes dimension; geometry appears to specify a full code | Announce six-bit addresses and separate site choice from logical words and rotations. |
| 17 | Examples fail to justify all cases; unsigned divisibility mistaken for signed test | State exhaustive within-block-bit versus only-block-bit cases; distinguish ordinary and signed counts. |
| 18 | Si used before definition; 64 and normalization unexplained | Coordinate evaluations first; independence from prior weight count spoken; display normalization count. |
| 19 | Stabilizer used before encoded states; translated sets assumed disjoint | Show permutation first; state disjointness as a checked property of chosen logical words. |
| 20 | W meaning or Gray address ordering changes silently | State fixed new pattern and printed row/column order; avoid a new sign symbol. |
| 21 | New row terminology and integer XOR expansion arrive together | Define row as an existing word; reuse pair intersection picture before triple. |
| 22 | Modular conditions appear arbitrary; stabilizer independence not explained | Connect divisors to coefficients and π/4; final formula includes every v in S. |
| 23 | Phase test seems to prove distance; six X checks seem complete | Explicitly separate the paper’s full-check distance result from gate verification. |
| 24 | New code family disconnected from story | Name the existing example; keep only degree-bounded evaluation and the nine-readout count. |
| 25 | Finite missing bit mistaken for asymptotic capacity theorem | Mark new long-block random-loss question; qualifiers visible, exact theorem kept in notes. |
| 26 | Too much Fourier machinery; learning promise too broad | Agreement picture and verbal interpretation; structured-learning qualification; no transform calculation. |
| 27 | Closing adds another result | Repeat established contributions and remain visible for questions. |
| Six backups | No reason or route to open them; missing prerequisites | Visible question, primary anchor, local definitions, and tested return destination for each. |

## Rehearsal still required

Ask a mathematically mature listener outside QEC to explain the message/address distinction, majority recovery, the two classical distances, equal phase within a pair, weights 24 and 32, and the difference between finite correction and capacity. Measure checkpoints at 11:30, 18:00, 27:30, 37:00, 39:00, 43:00, and 45:00. If late, shorten optional applications narration; preserve assumptions and the equal-phase argument.
