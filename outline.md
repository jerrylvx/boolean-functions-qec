# Boolean functions: applications in quantum error correction and beyond

## Scope and sequence

A 45-minute talk for mathematics, computer science, information theory, physics, and ECE audiences. Preserve the approved [abstract](abstract.md). The principal example starts with a completely specified classical encoder, becomes an eight-qubit encoding, and supplies the calculations needed to understand the author's 48-qubit construction. Adjacent applications follow that result. The closing slide returns to the research contributions.

The deck contains one title, 21 numbered main slides, seven additional reveal pages, and 18 backups, for 47 PDF pages. Six main slides have overlays. The timings include the two seven-second audience pauses and have not yet been measured in a listener rehearsal.

Error-correcting memory supplies the opening application. The eight-bit encoder is a teaching example, not a description of a particular memory product. The main talk does not claim that the 48-qubit construction is globally minimal.

## Timing

| Slides | Content | Minutes | Finish |
| --- | --- | ---: | ---: |
| Title, 1–7 | Memory errors, encoder, Boolean functions, ANF, derivatives, decoding, distance | 14 | 14:00 |
| 8–12 | Intersections, phase, encoded states, rotations, eight-qubit calculation | 9.5 | 23:30 |
| 13–17 | Error protection, 48-site geometry, labels, signs, overlap test, result | 10.5 | 34:00 |
| 18–20 | Reed–Muller codes, packing, erasure capacity, Fourier prediction | 9 | 43:00 |
| 21 | Contributions | 2 | 45:00 |

## Slide outline and delivery

### Title — 0.5 minute

Promise a specific result: “By the end, you will be able to follow an eight-bit error-correcting encoder and see how the same Boolean functions let us calculate a quantum gate.” Preview classical encoding, the quantum construction, and a short discussion of further applications. Introduce symbols when their calculations begin.

### 1. Correcting a bit error in memory — 1.5 minutes

Show message → encoder → stored bits → decoder. Define the encoder as the operation that computes stored bits from a message and the decoder as the operation that reconstructs the message from a readout. Assume at most one stored bit changes, at a location unknown to the decoder. The encoder and the allowed codewords are known to the receiver.

IBM's description supports the real motivation of correcting a memory bit error. The particular eight-bit example belongs to this exposition.

### 2. From four message bits to eight stored values — 2 minutes

Explain the XOR truth table before using its symbol. Separate four message coefficients `(b,a1,a2,a3)` from a three-bit position `u`. At an address, start with `b` and XOR each coordinate selected by its coefficient. The message `(0,1,1,1)` gives parity and the word `01101001` in lexicographic address order. Calculate the entry at `101` aloud.

### 3. Affine Boolean functions — 1.5 minutes

Define a Boolean function by its table. Name the encoder's formula an affine Boolean function. The constant coefficient toggles every output and each other coefficient selects a coordinate. Show the coordinate and constant-one examples. Define a codeword as an allowed stored word and the code as all 16 encoder outputs.

### 4. From a truth table to a polynomial — 2 minutes

Define algebraic normal form before abbreviating it, products as AND, and degree as the maximum number of variables in a nonzero monomial. Build the indicator of `000` one factor at a time. The received table is parity XOR this indicator. Expand it, then observe that its degree is three, so the table has left the affine code.

Do not claim that algebraic degree measures the number of corrupted entries. A single entry change creates several polynomial terms. Return to the different question of predictability on slide 20.

### 5. Comparing neighboring table entries — 2 minutes

Define the first-coordinate direction and calculate the comparison at `000,100` before displaying the derivative formula. The cube's labels are addresses, the circle values are received bits, and gold edges are the four disjoint first-direction comparisons. Use the caption “Derivatives of p and r along e1.” One changed vertex reverses exactly one comparison in each fixed direction. The derivative is a function of the input position, not a count of corrupted positions.

### 6. Recovering the four message coefficients — 2 minutes

Ask how to recover a selected coefficient. Toggling its coordinate cancels all other affine terms, so each edge supplies an estimate of that coefficient. Show the votes `0,1,1,1` for the first direction. Ask “Why is this majority reliable?” and wait about seven seconds. The second state reveals all three recovered coefficients, then removes their contributions from the received table. The residual `10000000` gives the constant by majority.

The algorithm works for any of the 16 messages and any zero-or-one-error pattern. The finite verification enumerates all 144 cases.

### 7. Why distinct codewords differ in at least four positions — 2.5 minutes

Define weight and Hamming distance through positions in a table. Pair cube vertices across a coordinate with nonzero coefficient. Each pair has exactly one output one. Display parity's four-element level set before naming an affine hyperplane. Draw points, not a Euclidean plane through parity's vertices.

The second state applies the count to the XOR of distinct affine functions. A nonconstant difference has weight four, the constant-one difference weight eight. Two codewords each one error away from the same readout would differ in at most two positions, which is impossible. Defer Reed–Muller terminology to slide 18.

Transition: “We have recovered the message and proved the guarantee. Next, we will use these same eight-entry functions to specify a quantum encoding.”

### 8. Counting intersections of Boolean supports — 2 minutes

Define support before using it. Coordinate faces are the level sets `u1=1` and `u2=1`. Their common edge has addresses `110,111`. Products select intersections, giving weights four, two, and one. Adding two weights counts a shared one twice while XOR counts it zero times. Subtract twice the intersection weight to derive the pair identity.

### 9. Single-qubit rotations produce phases — 2 minutes

Start with a unit vector with two complex components. Define computational basis vectors and ket notation through their column vectors, then illustrate relative phase in an equal superposition. Define T and its inverse, the eighth root of unity, and independent application to a binary basis word. Each one contributes one phase factor, so weight determines the phase. Specify the desired sign change on `111` before naming CCZ.

### 10. Encoding three qubits with complementary words — 2 minutes

Show three pairs of the previously defined affine words. Introduce their normalized equal superpositions. The eight pairs are disjoint, so the eight states are mutually orthogonal and encode three logical qubits. A physical operation that changes only phases preserves an encoded pair only when both words receive the same phase. Check that requirement before naming any logical action.

### 11. Choosing T and its inverse with parity — 1.5 minutes

Use the same labeled cube to assign T at parity zero and its inverse at parity one. The physical word equal to parity has four ones, all at inverse-rotation sites, so its signed count is minus four. Define signed weight as the positive count minus the negative count before displaying the summation formula. The physical pattern is fixed by addresses, not by the logical input.

### 12. Checking the eight-qubit logical gate — 2 minutes

Derive signed weight from distance to parity by considering the two possible parity values at one site. The affine count proves signed weight zero for every logical label other than `111`. For that label the two complementary words have counts minus four and plus four.

Keep phases concealed. Ask “Do +4 and −4 give different phases when each count contributes an angle of π/4?” Wait about seven seconds, then reveal the phases. Both exceptional words receive minus one. All other pairs receive plus one. This checks every encoded state, not just one representative per pair.

### 13. What additional error protection requires — 2.5 minutes

Define bit and phase errors by their action on basis vectors. Flipping all eight sites exchanges complementary words and leaves every encoded state unchanged. This supplies an example of a stabilizer check. A phase error changes its check outcome. Define a syndrome as the binary record of those outcomes, then show that two phase-error responses XOR.

A zero response column hides one phase error. Equal columns cancel and hide two. Define quantum distance in terms of undetected changes to encoded information. The toy code has distance two. Distance three is needed to correct an arbitrary error on one qubit. CSS terminology and dual-space calculations remain in backup.

### 14. Deleting a subspace leaves weights 24 and 32 — 2 minutes

Define four coordinates `u`, two coordinates `w`, and the retained evaluation set before using them. The full binary six-dimensional space has 64 points. Delete the 16 points with `w=00`, leaving the three displayed 16-point blocks.

Define the coefficient vectors and binary dot products. Every nonzero linear function has 32 ones by the same pairing argument as slide 7. Restricting to the deleted subspace leaves a nonzero function of `u`, with eight ones, or the zero function. Subtract to obtain 24 and 32. The zero function remains implicit in the displayed nonzero cases. Conclude orally that both weights are divisible by eight.

### 15. Completing the 48-qubit code — 2 minutes

The six coordinate evaluation words specify flip checks. Their combinations give 64 words in the stabilizer space. Three logical functions specify which translate of this space occurs in each encoded basis state. The sign function independently chooses T or its inverse at every site. Show the actual rotation diagram, with its row and column ordering visible.

All 64 terms in a state must receive the same phase. The site geometry alone does not supply the logical functions or signs. The full functions and sign polynomial are available in backup. The verified logical words produce eight disjoint sets of 64 words.

### 16. Checking phases through row intersections — 3 minutes

Define generator rows as the nine evaluation words already used. Products of rows select intersecting supports. Expand binary XOR as an integer expression, keeping the two additions distinct. Define signed weight using site signs and explain congruence as equality of remainders.

Reveal individual-row congruences, then pair congruences, then triple parities in fixed positions. The integer coefficients are 1, −2, and 4. Four or more distinct rows have coefficients divisible by eight. Stabilizer-containing triples are even. Only the logical triple is odd, producing the phase exponent `4 a1 a2 a3` modulo eight. The criterion makes the phase independent of the stabilizer word.

### 17. The resulting quantum code — 1 minute

State 48 physical qubits, three logical qubits, and quantum distance three before introducing the compact code notation. The code corrects any one-qubit error. The actual pattern has 26 forward and 22 inverse rotations and implements CCZ. Separate the explicit construction from the general test of row intersections.

Transition: “That completes the quantum construction. The classical example also lets us discuss three other questions: how much information a finite code can store, what happens on a probabilistic channel, and how predictable a Boolean output can be.”

### 18. Reed–Muller codes and finite-length bounds — 3 minutes

Name the classical example RM(1,3). Explain the degree-bounded family and define linearity and `[n,k,d]`. Each of 16 codewords has nine possible readouts with at most one error. Unique decoding requires disjoint sets, so `16 × 9 = 144 ≤ 256`. Name the Hamming bound after the count. The inequality is a necessary finite packing condition, not a new decoding algorithm or an equality claim.

### 19. Erasure recovery and channel capacity — 3 minutes

An erasure is a missing bit with a known location. The readout `?1101001` uniquely identifies parity. The readout `0??0?00?` admits both parity and the all-zero codeword, so four erasures can cause ambiguity.

Define independent erasure probability, rate, and asymptotic recovery before advancing. The second state states binary erasure capacity `1−ε`, defines optimal erasure decoding, and gives the Reed–Muller capacity result for a sequence of growing lengths with rates tending to any target in `(0,1)`. Whole-word recovery tends to probability one when the erasure probability is below `1−R`.

The cited theorem is Theorem 27 of Kudekar and coauthors. Its decoder uses the full compatible-codeword set. The theorem does not assert capacity for our fixed eight-bit decoder or promise a practical decoding complexity. The strict inequality matters.

### 20. Predicting a Boolean output with parity — 3 minutes

Return to the received cubic table. Define uniform input sampling and count seven agreements and one disagreement with parity. Only after that count, reveal the conversion of bits to real signs and the normalized Fourier coefficient. Agreements contribute plus one and disagreements minus one, so the average is `3/4` and the agreement probability is `(1+3/4)/2=7/8`.

Define a cryptographic Boolean component as computing one output bit from input bits. Accurate prediction by an affine function is undesirable for such a component. Degree three alone does not prevent the approximation seen here. Keep the full spectrum, transform nomenclature, and nearest-codeword formula in backup.

### 21. Contributions — 2 minutes

Return to the 48-qubit construction, its physical rotation pattern, and the exact signed-overlap test. State what was constructed and what was proved. Leave the slide visible throughout questions. Do not end with a new theorem or a slogan.

## Reveals

| Main slide | PDF pages | States | Concealed content |
| --- | --- | ---: | --- |
| 6 | 7–8 | 2 | Recovered coefficients and constant |
| 7 | 9–10 | 2 | General affine distance and unique recovery |
| 12 | 15–16 | 2 | Phase column and logical gate conclusion |
| 16 | 20–22 | 3 | Pairs, then triples and final logical phase |
| 19 | 25–26 | 2 | Capacity and asymptotic theorem |
| 20 | 27–28 | 2 | Sign conversion and Fourier coefficient |

The layout reserves hidden content so common equations stay stationary. The first Fourier state intentionally contains the observed seven-of-eight prediction count. The reveal explains its spectral expression rather than hiding an already observed count.

## Backups

Eighteen optional slides define the CSS description and the nine Campbell–Howard parity conditions, then cover affine input equivalence, translated errors, output-affine addition, syndrome rank under translation, polynomial support restrictions, higher derivatives, general Reed–Muller distance, degree versus rate, the full Fourier spectrum, integer inclusion–exclusion, the toy distance, the full signed-word test, the actual logical functions, the rotation polynomial, the qualified length exclusion, and sources.

The CSS, three-logical-qubit, phase-distance-at-least-three, and Campbell–Howard assumptions accompany the length exclusion. The interval 39–46 remains open. The 47-qubit statement concerns the particular code tested in the paper. No statement of global optimality is made. In the geometric reduction, distinguish a hyperplane through zero from an origin-avoiding hyperplane with a missing support point.

## Sources and verification boundaries

- [IBM, Troubleshooting Memory issues](https://www.ibm.com/support/pages/troubleshooting-memory-issues) supplies the memory context, not the eight-bit construction.
- [Kudekar et al., Reed–Muller Codes Achieve Capacity on Erasure Channels](https://arxiv.org/pdf/1601.04689), Theorem 27, supplies the asymptotic binary-erasure result under optimal block decoding. The theorem constructs a sequence with convergent target rate.
- [O'Donnell, Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf), Chapter 1, supplies the sign-correlation interpretation. The numeric example is calculated directly.
- Carlet, MacWilliams–Sloane, and Huffman–Pless provide the standard Boolean and coding background. The deck does not depend on a tour of external frontier results.
- The current manuscript supplies the six coordinate rows, fixed logical functions, exact sign polynomial, signed-overlap criterion, distance parameters, and qualified length exclusion. The standalone source has no build dependency on the manuscript repository.

Finite checks enumerate the 144 classical decoding cases, affine distances, toy phases, 63 nonzero six-variable linear functions, 129 signed row/pair/triple conditions, and 512 encoded-word phases. Checks also confirm the 26/22 signs, exact quantum distances, erasure examples, finite packing, Fourier coefficient, and rank-three/rank-two backup example. A clean local build and inspection of every reveal establish artifact correctness. The capacity theorem is checked against its source, not proved by these finite tests.

An outside-listener rehearsal remains a human acceptance step. Ask the listener to explain the encoder's four message bits versus three address bits, why both words of an encoded pair need equal phase, and why a finite distance guarantee differs from channel capacity. Measure the 45-minute timing in that rehearsal.
