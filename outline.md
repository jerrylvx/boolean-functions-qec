# Boolean functions: applications in quantum error correction and beyond

## Scope and sequence

This 45-minute talk is for audiences in mathematics, computer science, information theory, physics, and ECE. The approved [abstract](abstract.md) remains unchanged. One explicit encoder supplies the definitions, calculations, and notation used in the classical and quantum parts. The author's 48-qubit construction is completed before the shorter discussion of adjacent applications.

The deck contains one title page, 21 numbered main slides, seven additional reveal pages, and six backup slides, for 35 PDF pages. Six main slides use overlays. The two seven-second audience pauses are included in the timing. A rehearsal with a listener outside quantum error correction remains pending.

Error-correcting memory motivates the opening. The eight-bit encoder is a teaching example. It is not presented as the design of a particular memory product. The main talk does not claim that the 48-qubit construction is globally minimal.

## Timing

| Slides | Content | Minutes | Finish |
| --- | --- | ---: | ---: |
| Title and 1–6 | Memory errors, explicit encoder, ANF, derivatives, decoding | 12 | 12:00 |
| 7–9 | Intersections, minimum distance, classical recap | 6 | 18:00 |
| 10–13 | Quantum phases and complete eight-qubit gate calculation | 8 | 26:00 |
| 14–17 | 48-qubit construction and result | 8 | 34:00 |
| 18–20 | Reed–Muller codes, channel capacity, Fourier prediction | 9 | 43:00 |
| 21 | Contributions | 2 | 45:00 |

## Main slides

### Title, 0.5 minute

Promise a concrete calculation: “By the end, you will be able to follow an eight-bit error-correcting encoder and see how the same Boolean functions let us calculate a quantum gate.” Keep the omitted roadmap and memory citation in the notes.

### 1. Correcting one bit of error in memory, 1.5 minutes

Show a four-bit message entering an encoder, eight stored values, one changed value in the memory readout, and a decoder. Define encoding and decoding through these operations. State that at most one stored bit changes and that its position is unknown to the decoder. Explain that the eight-bit construction is a teaching example motivated by error-correcting memory.

### 2. The encoder evaluates eight XOR expressions, 2.5 minutes

Define XOR by its four input pairs. Separate the message bits `(b,a1,a2,a3)` from the three-bit address `u`. Display every stored value in two four-column panels. Substitution of `(0,1,1,1)` gives `01101001`. Explain that the extra positions add constraints without adding message information.

### 3. Affine Boolean functions define the codewords, 1.5 minutes

Define a Boolean function and then define the displayed encoder as an affine Boolean function. Define the evaluation map. Recover an uncorrupted message by

\[
b=f(000),\qquad a_i=f(e_i)\oplus f(000).
\]

This proves that the 16 messages give 16 distinct codewords. The code is the set of these selected eight-bit words.

### 4. From a truth table to a polynomial, 2 minutes

Define algebraic normal form, monomials, and degree before using them. Define `r` as the Boolean function whose table is the eight bits read from memory. Show the original and corrupted words before writing

\[
r=p\oplus\delta_{000}.
\]

Evaluate the indicator at `000` and away from `000`, then expand the polynomial. The degree-three readout is outside the affine code. Do not identify polynomial degree with the number of errors.

### 5. Comparing neighboring table entries, 2 minutes

Define a direction vector and compute the `000,100` comparison before using the Boolean derivative. Label the cube addresses, values, changed entry, and selected edges. The visible caption is “Derivatives of p and r along e1.” The changed endpoint reverses that comparison from one to zero. The other three first-direction comparisons remain one. State that the same reasoning applies in each coordinate direction.

### 6. Recovering the four message coefficients, 2 minutes

Derive `D_ei f = ai`. Show the four first-direction votes. Ask “Why is this majority reliable?” and wait seven seconds. Reveal that one changed address can spoil only one of four disjoint comparisons. Recover all three `a_i`, remove their contributions, and recover `b` from seven equal residual values.

### 7. Support intersections compute Hamming distance, 2 minutes

Define support and weight:

\[
\operatorname{supp}(f)=\{u:f(u)=1\},\qquad
\operatorname{wt}(f)=|\operatorname{supp}(f)|=\sum_u f(u).
\]

Define the Hamming distance of a particular pair of evaluation words:

\[
d_H(f,g)=|\{u:f(u)\ne g(u)\}|=\operatorname{wt}(f\oplus g).
\]

Use two coordinate faces and their common edge to derive the pair-weight identity. Calculate `d_H(u1,u2)=4+4-2(2)=4` immediately after the identity.

### 8. The code's minimum distance is four, 2.5 minutes

Define the code-level minimum

\[
d_{\min}(C)=\min_{f\ne g\in C}d_H(f,g).
\]

For a nonconstant affine difference, pair vertices across a coordinate with nonzero coefficient to obtain four ones. The constant-one difference has eight ones. Slide 7 supplies a pair at distance four, so `d_min(C)=4`.

Name the parity-zero level set as a linear hyperplane through zero. Name the parity-one level set as its affine translate. On the second state, prove unique one-error correction by

\[
4=d_{\min}(C)\le d_H(f,g)
\le d_H(f,r)+d_H(r,g)\le2.
\]

### 9. What the classical example established, 1.5 minutes

Recap the complete calculation: affine evaluations encode, ANF describes the damaged table, derivatives recover coefficients, and minimum distance proves unique correction. Keep

\[
d_H(p,r)=1,\qquad d_{\min}(C)=4
\]

side by side. The first value describes one readout and one codeword. The second is the smallest distance between any two codewords.

### 10. Single-qubit operations change bits and phases, 2 minutes

Define a qubit and computational basis vectors before introducing ket notation. Show the action of a bit flip and a phase sign change. Define `T`, `T†`, and the phase acquired by a binary basis word. State the desired sign on logical label `111` before naming CCZ.

### 11. Encoding three qubits with complementary words, 2 minutes

Build each encoded basis state from the two previously defined affine words with constants zero and one. Explain why eight disjoint pairs give eight orthogonal states. The all-site bit flip exchanges the two words and leaves their sum fixed. A physical phase operation must give both words in a pair the same phase.

### 12. Choosing T and T† with parity, 1.5 minutes

Reuse the labeled cube. Define the physical choice of `T` or `T†` at every address. Count an explicit word, then define signed weight as an ordinary integer. Connect the signed count to the accumulated physical phase.

### 13. Checking the eight-qubit logical gate, 2.5 minutes

Derive signed weight from distance to parity. Show the signed counts before the phase column. Ask whether `+4` and `-4` produce different phases when every count contributes `π/4`, then wait seven seconds. Reveal that both phases are minus one. Check both words in all eight complementary pairs and conclude logical CCZ.

### 14. Deleting a subspace leaves weights 24 and 32, 2 minutes

Explain why the toy encoding lacks full one-qubit protection. Split each six-bit address into `u` and `w`, then define the retained set before showing the three 16-point blocks. Every nonzero linear function has 32 ones on the 64-point space. Its restriction to the deleted subspace has eight or zero ones, producing `32-8=24` or `32-0=32`.

### 15. Completing the 48-qubit code, 2 minutes

Define the coordinate evaluation words and their 64-word span. A coordinate bit flip permutes the terms of every encoded state. Define a stabilizer check as an operation that leaves every encoded state fixed. Then introduce the three logical functions, the encoded superposition, the sign function, and the physical rotation diagram. Keep the roles of sites, logical labels, and signs separate.

### 16. Checking phases through row intersections, 3 minutes

Define a generator row as one of the nine displayed evaluation words. Define coordinatewise products through support intersections. Expand XOR over the ordinary integers, then introduce signed congruences in three fixed reveal states. Individual rows appear first, pairs second, and triples third. Explain why terms using four or more rows disappear modulo eight. The logical triple supplies the remaining odd term.

### 17. The resulting quantum code, 1 minute

State 48 physical qubits and three logical qubits. Define quantum distance `d_Q` as the smallest physical support of an undetected logical error, then state `d_Q=3`. Only after the definition introduce `[[48,3,3]]`. State the `26T+22T†` implementation of logical CCZ and distinguish the explicit construction from the general overlap test.

### 18. Reed–Muller codes and finite-length bounds, 3 minutes

Name the classical code `RM(1,3)` and define the degree-bounded family. Define `[n,k,d_min]`. Count nine zero-or-one-error readouts around each codeword, so disjoint decoding sets require `16(1+8)=144≤256`. Explain what is counted before naming the Hamming bound.

### 19. Erasure recovery and channel capacity, 3 minutes

Define a known-location erasure. Show one uniquely recoverable readout and one ambiguous four-erasure readout. Define rate, independent erasure probability, and asymptotic reliable recovery. On the second state, state `C=1-ε` and the Reed–Muller capacity result under optimal block decoding. Keep this growing-length theorem distinct from the finite decoder used earlier.

### 20. Predicting a Boolean output with parity, 3 minutes

Count seven agreements and one disagreement before introducing sign encoding. Define uniform sampling and the normalized Fourier coefficient. Derive the value `3/4` and prediction probability `7/8`. Explain why accurate affine prediction is undesirable for a cryptographic Boolean component. Return to slide 4 to show that degree three did not prevent this approximation.

### 21. Contributions, 2 minutes

Return to the explicit 48-qubit code, the physical rotation pattern, and the signed-overlap verification. Leave this slide visible during questions.

## Reveals

| Main slide | PDF pages | States | Concealed content |
| --- | --- | ---: | --- |
| 6 | 7–8 | 2 | Majority explanation, recovered coefficients, and constant |
| 8 | 10–11 | 2 | Unique-correction contradiction |
| 13 | 16–17 | 2 | Phase column and logical-gate conclusion |
| 16 | 20–22 | 3 | Pair conditions, then triple conditions and logical phase |
| 19 | 25–26 | 2 | Capacity and asymptotic theorem |
| 20 | 27–28 | 2 | Sign conversion and Fourier coefficient |

The layout reserves space for concealed material. Common equations and diagrams remain stationary between states. The first Fourier state contains the observed agreement count. The reveal explains its spectral expression.

## Backups

The six backup slides cover input-affine equivalence, the explicit two-site logical phase error in the toy code, the 48-qubit logical functions, the rotation-sign polynomial, the qualified length exclusion, and sources.

The length backup defines CSS codes, `d_Z≥3`, and the Campbell–Howard conditions locally. It states the hypotheses for the `n≤38` exclusion, leaves `39≤n≤46` open, and limits the 47-qubit statement to the specified code. Advanced classifications, rank-translation examples, polynomial reductions, and the full Fourier spectrum remain outside the deck.

## Sources and verification boundaries

- [IBM, Troubleshooting Memory issues](https://www.ibm.com/support/pages/troubleshooting-memory-issues) supplies the memory context. It does not supply the eight-bit construction.
- [Kudekar et al., Reed–Muller Codes Achieve Capacity on Erasure Channels](https://arxiv.org/pdf/1601.04689), Theorem 27, supplies the asymptotic binary-erasure result under optimal block decoding.
- [O'Donnell, Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf), Chapter 1, supplies the sign-correlation interpretation.
- Carlet, MacWilliams–Sloane, and Huffman–Pless supply standard Boolean-function and coding terminology.
- The current manuscript supplies the coordinate rows, logical functions, sign polynomial, overlap criterion, distances, and qualified lower-bound result. The standalone project has no build dependency on the manuscript repository.

Finite checks enumerate all 16 encoder outputs, 144 zero-or-one-error decoding cases, every pair of affine codewords, all toy phases, 63 nonzero six-variable linear functions, 129 row-intersection conditions, and 512 encoded-word phases. The checks also cover the erasure examples, finite packing count, Fourier coefficient, sign count, and stated distances. Compilation and rendered-page inspection establish artifact correctness. They do not establish the 45-minute pacing.
