# Boolean functions: applications in quantum error correction and beyond

## Structure and timing

The approved [abstract](abstract.md) is unchanged. The talk assumes mathematical maturity but no Boolean-function, coding-theory, or QEC background. One eight-bit example supplies the functions, counts, and quantum gate calculation; the 48-qubit construction follows before a short applications discussion.

The three questions are: How do eight stored values protect four message bits? How do counts determine quantum phases? How does the 48-qubit construction satisfy the required counts?

The deck has **27 numbered main slides, six backup frames, and 61 PDF pages**: one title, 27 main frames, 25 extra main reveal pages, six backup frames, and two extra backup reveal pages. Twenty-one main frames use overlays; the logical-function backup has three states. Timing includes the two seven-second audience pauses.

| Portion | Time | Duration |
|---|---|---:|
| Title and 1–6: construct and decode | 00:00–11:30 | 11:30 |
| 7–10: intersections, distance, recap | 11:30–18:00 | 6:30 |
| 11–15: eight-qubit gate | 18:00–27:30 | 9:30 |
| 16–23: 48-qubit code and test | 27:30–37:00 | 9:30 |
| 24: Reed–Muller family and packing | 37:00–39:00 | 2:00 |
| 25–26: visual applications overview | 39:00–43:00 | 4:00 |
| 27: contributions | 43:00–45:00 | 2:00 |

## Detailed running order

| Slide | Time | Duration | Focus and essential notation | PDF pages |
|---|---|---:|---|---|
| Title | 00:00–00:30 | 00:30 | None | 1 |
| 1. Correcting one bit of error in memory | 00:30–01:30 | 01:00 | Encoder, decoder, message, readout | 2 |
| 2. The encoder evaluates eight XOR expressions | 01:30–04:00 | 02:30 | XOR ⊕; message b,a₁,a₂,a₃; a=(a₁,a₂,a₃); address u=(u₁,u₂,u₃); fₐ,ᵦ | 3–4 |
| 3. Affine Boolean functions define the codewords | 04:00–05:30 | 01:30 | Boolean function; affine; e₁=100,e₂=010,e₃=001; codeword; C | 5 |
| 4. From a truth table to a polynomial | 05:30–07:30 | 02:00 | p: parity; r: readout; algebraic normal form (ANF); degree | 6–8 |
| 5. Comparing neighboring table entries | 07:30–09:30 | 02:00 | Direction eᵢ; Boolean derivative Dₑᵢf | 9–10 |
| 6. Recovering the four message coefficients | 09:30–11:30 | 02:00 | Reuse Dₑᵢf, aᵢ, b; majority; residual values | 11–12 |
| 7. Intersections count differing positions | 11:30–13:15 | 01:45 | Support in words; wt(f); Hamming distance d_H(f,g) | 13–14 |
| 8. Nonconstant affine functions have four ones | 13:15–15:00 | 01:45 | Affine hyperplane; reuse p and eᵢ | 15–16 |
| 9. Minimum distance makes correction unique | 15:00–16:45 | 01:45 | d_min(C), distinct from d_H(f,g) | 17–18 |
| 10. What the classical example established | 16:45–18:00 | 01:15 | No new terms; d_H(p,r)=1 and d_min(C)=4 | 19 |
| 11. A quantum state has amplitudes and relative phase | 18:00–19:30 | 01:30 | Qubit; basis vectors $\lvert0\rangle$, $\lvert1\rangle$; amplitude; superposition; relative phase; bit and phase flip | 20–21 |
| 12. Single-qubit rotations add phase angles | 19:30–21:00 | 01:30 | T,T†; eⁱθ; physical basis word $\lvert v\rangle$ | 22–23 |
| 13. Complementary words encode three qubits | 21:00–23:30 | 02:30 | Logical label a; encoded state $\lvert a\rangle_L$; physical versus logical qubits | 24–25 |
| 14. Choosing rotations for a three-qubit sign change | 23:30–25:00 | 01:30 | CCZ; signed weight W(v) | 26–27 |
| 15. Checking every encoded pair | 25:00–27:30 | 02:30 | Reuse W, p, fₐ,ᵦ, d_H | 28–29 |
| 16. Selecting 48 physical positions | 27:30–28:15 | 00:45 | u now has four bits; w has two bits; six-bit address (u,w) | 30–31 |
| 17. The retained linear words have weights 24 and 32 | 28:15–29:45 | 01:30 | Linear means XOR of selected bits without a constant; reuse wt | 32–34 |
| 18. Summing stabilizer words gives an unchanged state | 29:45–30:45 | 01:00 | S₁,…,S₆; S; stabilizer | 35–36 |
| 19. Logical functions distinguish eight encoded states | 30:45–31:45 | 01:00 | K₁,K₂,K₃; K(a); reuse S and $\lvert a\rangle_L$ | 37–38 |
| 20. Assigning the physical rotations | 31:45–32:30 | 00:45 | Reuse T,T†,W; fixed 48-site pattern | 39 |
| 21. XOR produces intersection terms | 32:30–33:30 | 01:00 | Generator row; g₁,g₂,g₃ as distinct selections; coordinatewise product | 40–41 |
| 22. Signed intersections verify the logical gate | 33:30–35:30 | 02:00 | Congruence modulo 8,4,2; reuse W and generator rows | 42–44 |
| 23. The resulting quantum code | 35:30–37:00 | 01:30 | Stabilizer check; d_Q; [[48,3,3]] | 45 |
| 24. Reed–Muller codes and finite packing | 37:00–39:00 | 02:00 | RM(d,m); linear code; [n,k,d_min]; Hamming bound | 46–47 |
| 25. Recovering missing data and approaching capacity | 39:00–40:45 | 01:45 | Erasure; rate; capacity; no new mathematical symbols | 48–49 |
| 26. Predicting outputs, learning, and cryptography | 40:45–43:00 | 02:15 | Fourier analysis; statistical learning; reuse parity and r | 50–52 |
| 27. Contributions | 43:00–45:00 | 02:00 | No new notation or claims | 53 |

## Explanation and reveal cues

### Title. Title — 00:00–00:30

Promise: We will construct a small error-correcting code, then use the same Boolean-function calculations to understand a quantum gate. Basic arithmetic is sufficient to start; explain the quantum vector notation when it arrives.

**Reveals:** One title page. Keep the promise spoken; do not restore the deleted title-page roadmap.

**Transition:** Begin with writing a message into memory.

### 1. Correcting one bit of error in memory — 00:30–01:30

Point from four message bits to eight stored values and then to the changed value. The decoder knows the encoder but not the changed position. Extra stored values create constraints without adding message information. Say that this is a teaching encoder motivated by error-correcting memory, not the design of a particular device.

**Reveals:** One state. State the at-most-one-error assumption before claiming correction.

**Transition:** We must specify how each of those eight bits is computed.

### 2. The encoder evaluates eight XOR expressions — 01:30–04:00

Read the four XOR outcomes; products of bits mean AND. Message coefficients remain fixed while the address runs through eight positions. Point to column 101: b XOR a₁ XOR a₃ gives 0 XOR 1 XOR 1 = 0. The general expressions specify all sixteen messages, not just the displayed example.

**Reveals:** State 1: message/address roles, formula, and expression rows. Compute column 101 aloud. State 2: reveal all example values and the complete stored word.

**Transition:** This encoder has a familiar mathematical description.

### 3. Affine Boolean functions define the codewords — 04:00–05:30

A Boolean function is the complete input-output table. An affine function is a constant XOR selected input bits. Introduce eᵢ before the recovery formula. The value at zero gives b; comparing zero with eᵢ gives aᵢ. Therefore no two messages encode to the same word. The receiver knows this family because it knows the encoder.

**Reveals:** One state. Read definitions, then demonstrate the recovery formulas, then infer sixteen distinct codewords.

**Transition:** Now inspect the actual readout as a function too.

### 4. From a truth table to a polynomial — 05:30–07:30

Point first to p and r. At 000 every factor of (1 XOR u₁)(1 XOR u₂)(1 XOR u₃) is one; elsewhere some factor vanishes. Expanding cancels parity’s linear terms. ANF is a description of the damaged table, not a step the decoder must perform. Degree counts variables in the largest product term, not errors.

**Reveals:** State 1: original and corrupted words. State 2: construct the indicator product. State 3: name ANF, expand, and compare degree with the code family.

**Transition:** To decode, compare neighboring table entries.

### 5. Comparing neighboring table entries — 07:30–09:30

Read the values at 000 and 100 before the derivative formula. Changing an input address is not corrupting a stored output. The changed entry belongs to one disjoint edge in each fixed direction; the other three comparisons remain intact. The derivative is 1 when moving along that edge changes the output.

**Reveals:** State 1: cube and the explicit endpoint comparison. State 2: derivative formula and four-edge table.

**Transition:** For an affine function, every comparison in one direction should give the same coefficient.

### 6. Recovering the four message coefficients — 09:30–11:30

Toggling uᵢ cancels terms independent of uᵢ. Ask: Why is this majority reliable? Wait seven seconds. One changed address can spoil only one vote, leaving at least three correct votes. All three directions work the same way. After recovering a, XOR its contribution out of every readout entry; at least seven residuals equal b.

**Reveals:** State 1: derivative identity and votes, with the question. State 2: majority argument, coefficients, residual word, and constant. Do not give the explanation before the pause.

**Transition:** We have a decoder. Now explain why no other allowed message can fit the same corrupted readout.

### 7. Intersections count differing positions — 11:30–13:15

The support is the positions with value one; weight counts them. Point to the two colored coordinate faces and common edge. Four plus four counts the intersection twice, whereas XOR excludes it. Subtract two copies of the two-point overlap. Weight arithmetic is ordinary integer arithmetic.

**Reveals:** State 1: faces, counts, and overlap reasoning. State 2: general identity, definition of pairwise distance, and d_H(u₁,u₂)=4.

**Transition:** The same four-versus-four count holds for any nonconstant affine function.

### 8. Nonconstant affine functions have four ones — 13:15–15:00

Choose a coordinate with a nonzero coefficient. Its four pairs each contain exactly one one. Introduce the geometry only after the count: inputs giving a specified output form an affine hyperplane. Parity’s zero set is a linear hyperplane through zero; its one set is a translate. Do not draw a Euclidean plane through the four parity-one vertices.

**Reveals:** State 1: paired cube and four ones. State 2: geometric name and parity-one addresses. Backup trigger: Does changing the binary coordinates change these counts or the code?

**Transition:** Apply this count to the difference between two allowed codewords.

### 9. Minimum distance makes correction unique — 15:00–16:45

The XOR of two distinct affine words is nonzero affine: four ones if nonconstant, eight if constant. The earlier coordinate pair attains four, so the minimum is exactly four. If two candidates were each within one change of r, joining those changes would put them within two of one another. This contradicts their minimum separation.

**Reveals:** State 1: define and establish d_min(C)=4. State 2: two hypothetical candidates, the distance chain, and unique correction.

**Transition:** Review what is now fully established before changing physical setting.

### 10. What the classical example established — 16:45–18:00

Point through affine evaluation, polynomial description, derivative recovery, and unique correction. The observed one-bit corruption is a distance between one word and one readout. The minimum distance belongs to the entire code. Neither statement replaces the other.

**Reveals:** One state; this is a recap, not another proof.

**Transition:** The sixteen classical words form eight complementary pairs. Each pair will represent one quantum basis state.

### 11. A quantum state has amplitudes and relative phase — 18:00–19:30

Read the two basis vectors before using their kets in a sum. Amplitudes are complex coefficients whose squared magnitudes sum to one. The equal sum is normalized by 1/√2. A phase flip changes the relative sign of its two components; multiplying both by the same unit complex factor does not change the physical state. A bit flip exchanges the two basis vectors.

**Reveals:** State 1: basis and normalized superposition. State 2: relative versus overall sign; then bit flip.

**Transition:** The physical operation in the construction rotates one amplitude by a fixed angle.

### 12. Single-qubit rotations add phase angles — 19:30–21:00

The circle represents a unit complex multiplier, not a Bloch sphere. Introduce i and the angle notation. T fixes |0⟩ and multiplies the |1⟩ amplitude by a forward π/4 phase; T† reverses it. A string inside a ket labels the physical bits. In 00101 there are two ones, so the two factors multiply and their angles add.

**Reveals:** State 1: rotation arrows and the single-qubit action. State 2: explicit word and weight-to-phase formula.

**Transition:** We need these rotations to act correctly on an encoded superposition.

### 13. Complementary words encode three qubits — 21:00–23:30

Show a=000 first: the all-zero and all-one words form a normalized pair. Each of the eight labels has two distinct physical words, and no word is shared between pairs; this gives orthogonal states. Their arbitrary superpositions encode three logical qubits. The hardware uses eight physical qubits. For one encoded pair, unequal phases would change the ratio between its two amplitudes and take it outside the intended one-dimensional pair state.

**Reveals:** State 1: complementary table and normalized pair. State 2: eight encoded states and equal-phase requirement. Orally compare a plus pair with a plus/minus pair using the preceding slide.

**Transition:** Specify the desired operation on the logical labels, then choose physical rotations.

### 14. Choosing rotations for a three-qubit sign change — 23:30–25:00

State the desired change: only logical 111 gets a minus sign. Name controlled-controlled-Z afterward. The address determines the physical rotation once and for all. For the word p, its four ones are all at inverse rotations, giving signed count −4. W counts ones with signs; it does not count addresses with parity one independently of v.

**Reveals:** State 1: logical target, rotation cube, and explicit count. State 2: signed-weight definition and physical phase.

**Transition:** Check both physical words at every logical label.

### 15. Checking every encoded pair — 25:00–27:30

At parity-zero addresses, XOR with p leaves v; at parity-one addresses, subtracting p turns the contribution into −v. Summing gives W(v)=d_H(p,v)−4. If a differs from 111, the affine difference is nonconstant. At 111, the two words are parity and its complement. Ask whether +4 and −4 give different phases and wait seven seconds. Both phases are −1; equal phase within each pair and label dependence together establish CCZ.

**Reveals:** State 1: identity and count table with phase cells blank. State 2: fixed-position phase entries and conclusion. The question/conclusion share a reserved area.

**Transition:** The gate calculation works. The next construction adds protection against an arbitrary one-qubit error.

### 16. Selecting 48 physical positions — 27:30–28:15

Explicitly announce that u is now a four-bit within-block address; the previous cube used three bits. The two bits w label four blocks. Delete w=00 and retain three blocks of sixteen sites. The toy code’s limitation motivates a larger construction; geometry alone does not complete the code.

**Reveals:** State 1: all four blocks. State 2: cross out the zero block and count 48. Backup trigger: Why does the eight-qubit code not already correct every one-qubit error?

**Transition:** Evaluate linear functions on the retained positions and count their ones.

### 17. The retained linear words have weights 24 and 32 — 28:15–29:45

Every nonzero linear function on six bits has 32 ones. If a within-block bit occurs, its restriction to the deleted block is still nonzero linear, with eight ones. Otherwise a nonzero function of w is zero on the deleted block. Use u₁ and w₁ as examples of these exhaustive cases. The zero function gives weight zero. Divisibility of ordinary weights does not by itself prove the signed phase conditions.

**Reveals:** State 1: the full-space count. State 2: u₁ and 32−8. State 3: w₁ and 32−0; distinguish ordinary from signed counts.

**Transition:** The six coordinate evaluation words generate the superpositions used by the code.

### 18. Summing stabilizer words gives an unchanged state — 29:45–30:45

The six coordinate words are independent: no nonzero linear combination vanishes on all retained sites, since its weight is 24 or 32. Thus six binary choices give 64 distinct words. Their equal-amplitude sum has normalization 1/8. A mask Sᵢ specifies physical bits to flip; it does not change the coordinate labels. Adding the same mask permutes the collection.

**Reveals:** State 1: six words, their combinations, and normalized sum. State 2: paired summands and the stabilizer name. The next slide verifies the operation on every encoded label.

**Transition:** Choose different disjoint collections to store the eight logical labels.

### 19. Logical functions distinguish eight encoded states — 30:45–31:45

For a=100, shift every word by K₁. The logical functions are chosen so that the eight shifted collections are disjoint; this is a checked property of the construction, not a consequence of site geometry alone. Adding Sᵢ permutes each shifted collection, fixing every encoded state. Other phase-type checks are part of the completed code; the six displayed operations are not asserted to be its entire check set.

**Reveals:** State 1: logical words and one translated collection. State 2: the general encoded-state formula and invariance. Backup trigger: What are the actual logical functions?

**Transition:** Now assign a physical rotation at every retained position.

### 20. Assigning the physical rotations — 31:45–32:30

Point to the row and column order before reading a site. The block counts are 6,6,10 inverse rotations. W has the same meaning as before, but now uses this fixed 48-site pattern. The sign polynomial is optional detail; the visible pattern is the actual verified construction.

**Reveals:** One state. Backup trigger: How is this rotation pattern specified?

**Transition:** We can verify all encoded phases using counts of row intersections.

### 21. XOR produces intersection terms — 32:30–33:30

A generator row is simply one of the three logical words or six stabilizer words. Recall the two-face count before the three-row expression. These are integer identities: XOR has been expressed using ordinary plus, minus, and products. At a site shared by all three rows, the first two groups contribute 3−6; adding 4 restores the XOR value 1.

**Reveals:** State 1: pair identity and recalled picture. State 2: three-row expansion and coefficients 1,−2,4.

**Transition:** Weight these integer contributions by the fixed physical rotation signs.

### 22. Signed intersections verify the logical gate — 33:30–35:30

Adding eight to W adds 2π to the angle. Thus only its remainder modulo eight matters. A row contribution must vanish modulo eight; a pair contribution is multiplied by −2, so divisibility by four suffices. A triple is multiplied by four, so only its parity matters. The logical triple is odd and all other triples even. Higher XOR-expansion coefficients are multiples of eight. The resulting W is independent of the selected stabilizer word, while its logical-label dependence is exactly 4a₁a₂a₃.

**Reveals:** State 1: remainder explanation and row condition. State 2: pair condition. State 3: exact triple condition, higher-term explanation, and phase conclusion. Equations remain stationary.

**Transition:** This proves the gate for the displayed code and rotation pattern; state error protection separately.

### 23. The resulting quantum code — 35:30–37:00

A check tests whether a stabilizer has its expected value. Quantum distance refers to the smallest support of an undetected nontrivial logical product of bit and phase flips. The paper establishes distance three using all code checks, so the code corrects an arbitrary one-site error. The signed-overlap calculation alone does not establish distance. The construction, distance proof, and exact gate criterion are distinct research results.

**Reveals:** One state. Backup trigger: Is 48 the smallest possible length? Keep all restrictions in the backup answer.

**Transition:** That completes the quantum construction. The classical example also belongs to a much larger family of codes.

### 24. Reed–Muller codes and finite packing — 37:00–39:00

Name RM(1,3) only now. More generally evaluate all Boolean polynomials of degree at most d at every m-bit address. Closed under XOR means linear. Point to n=8 stored bits, k=4 message bits, and minimum distance four. Each center in the picture represents a codeword, and its eight neighbors represent single-bit changes. The circles are schematic sets, not Euclidean geometry. Count nine readouts for each of sixteen messages.

**Reveals:** State 1: family and parameters. State 2: packing picture and 144≤256. Do not introduce the general binomial packing formula.

**Transition:** What changes when positions are known to be missing rather than silently flipped?

### 25. Recovering missing data and approaching capacity — 39:00–40:45

Point to the question-mark cell. Its location is known, unlike our earlier bit error. Rate means information bits per transmitted bit. Capacity is an asymptotic benchmark for a specified random channel, not a guarantee for every finite loss pattern. For independent erasures, suitable growing Reed–Muller sequences achieve that benchmark under optimal whole-block decoding. No efficient-decoder claim is being made.

**Reveals:** State 1: erasure picture and finite recovery. State 2: verbal definitions and qualified asymptotic result. Keep the exact theorem in the source note below.

**Transition:** The same functions can also be studied as computations whose outputs we want to predict.

### 26. Predicting outputs, learning, and cryptography — 40:45–43:00

Read the seven agreements and one disagreement under equally likely inputs. Fourier analysis measures correlations with parity patterns; the statement is a verbal summary, with no transform formula to derive. Recall derivatives as a way to ask whether changing an input changes the output. Learning uses input-output examples to predict new outputs; appropriate function structure can make this possible. Do not imply arbitrary Boolean functions are efficiently learnable. Predictability can be useful for learning and undesirable for a cryptographic component. Degree three alone did not prevent this strong parity approximation.

**Reveals:** State 1: agreement cells. State 2: Fourier interpretation. State 3: examples-to-predictions picture and learning/cryptographic implications.

**Transition:** The broader applications ask different questions about Boolean functions. My construction uses their evaluation words and intersection counts to control an encoded quantum gate.

### 27. Contributions — 43:00–45:00

Repeat the three contributions: explicit protected encoding, the 26T+22T† implementation, and the exact phase criterion. Connect the opening weight count to the final intersection calculation. Leave the contributions visible throughout questions; use the backup links only when their questions arise.

**Reveals:** One state. Backup trigger: Where can I read more?

**Transition:** Stop after the contributions; invite questions without adding a new topic.

## Backup navigation

Backups answer optional questions; the main argument does not require visiting them. Click the button on the primary anchor, then use the return button to land on its final reveal.

| Backup | Anchor | Trigger question | PDF pages |
|---|---:|---|---|
| Affine equivalence | 8 | Does changing the binary coordinates change these counts or the code? | 54 |
| Toy quantum distance | 16 | Why does the eight-qubit code not already correct every one-qubit error? | 55 |
| Explicit logical functions | 19 | What are the three logical functions? | 56–58 |
| Rotation-sign polynomial | 20 | How is this rotation pattern specified? | 59 |
| Qualified length exclusion | 23 | Is 48 the smallest possible length? | 60 |
| Sources | 27 | Where can I read more? | 61 |

## Notation discipline

Use p for the original parity table, r for the readout, and C for the classical code. Do not add Enc, a named error indicator, support-set notation, hyperplane names, finite-field notation, a phase constant, or separate signed-weight subscripts. W(v) always counts ones at forward rotations minus ones at inverse rotations for the currently fixed physical pattern. Announce the change of pattern and the change in address dimension. Keep d_H, d_min, and d_Q distinct.

The six coordinate words and three logical words retain their names because their different roles are needed in the encoded-state formula and the exact gate test. The sign polynomial is defined only in its backup.

## Sources and acceptance

- The current manuscript supplies the logical functions, sign polynomial, exact signed-intersection test, distances, and qualified lower bound. The standalone build does not depend on the manuscript workspace.
- [Kudekar et al., Theorem 27](https://arxiv.org/pdf/1601.04689): suitable growing Reed–Muller sequences achieve binary-erasure capacity under optimal whole-block decoding.
- [O’Donnell, Chapters 1–3](https://arxiv.org/pdf/2105.10386): parity correlations, input influence, and structured learning. No generic efficient-learning claim is made.
- [Winston’s heuristics](https://courses.csail.mit.edu/6.141/spring2010/pub/debates/Talk/phw.html): opening promise, a central example, examples before abstractions, explicit transitions, pauses, and repeated contributions.

Finite checks, compilation, rendered-page inspection, and link verification establish artifact properties. An outside-listener rehearsal must still establish comprehension and pacing. Nothing in this revision requests publication.
