# Boolean functions: applications in quantum error correction and beyond

## Story and scope

A roughly 45-minute presentation for mathematics, computer science, information theory, physics, and ECE audiences. The deck contains a title, 20 numbered main slides, and 15 optional backup/reference slides. Four main slides have staged reveals, giving 41 PDF pages. The timing below reserves 26 minutes for the opening and Boolean fundamentals/applications, 17.5 minutes for QEC, and 1.5 minutes for the close. Audience pauses are included; questions after the talk are additional. The budget has not been measured in rehearsal. The title and abstract preserve the author's approved wording in [the abstract](abstract.md).

One experiment carries the exposition: encode four message bits as an affine Boolean truth table on a cube, corrupt one entry, and recover the message. ANF describes the received word; derivatives supply local checks; Fourier scores count agreement with parity. The very agreement that helps the receiver also illustrates an unwanted predictor of a cryptographic Boolean output. The same affine tables then form the encoded basis of an eight-qubit quantum code. A signed Hamming-weight identity verifies its logical gate. The current paper supplies the larger, distance-three construction and the precisely scoped length lower bound.

**One idea:** the same Boolean structure that helps recover a message can expose a predictable output—and can be deliberately chosen to implement a quantum gate. Hyperplanes interpret that structure geometrically within the existing chapters; geometry does not become another chapter.

| Chapter | Main slides | Question and completed result |
| --- | --- | --- |
| 1. Recover a message | 1–6 | Can a rule survive one damaged entry? Derivative votes recover the message; distance proves the guarantee. |
| 2. Understand a rule | 7–9 | What changes the output, and what predicts it? Derivatives test input sensitivity; one Fourier score measures agreement with an XOR rule. |
| 3. Control a gate | 10–20 | Can those counts be designed to produce a useful operation? Geometry and signed weights lead to the paper's protected logical CCZ. |

The title previews these chapters; a short footer identifies the current chapter on every main slide. Spoken transitions at slides 7 and 10 state what was established and the next question. No extra section-divider slides are needed.

### Match to the advertised abstract

| Abstract promise | Concrete treatment in the main talk |
| --- | --- |
| Algebra | ANF of parity and the one-entry corruption, slide 3. |
| Geometry | Cube edges, parity's affine hyperplane, intersecting coordinate hyperplanes, and whole space minus a subspace, slides 4, 6, 7, 10, 16. |
| Fourier analysis | One unnormalized Walsh score and the eight-value spectrum of the same received table, slide 8. |
| Recovering messages from noise | Complete majority decoding and its distance guarantee, slides 1–6. |
| Effect of changing individual inputs | Observing one input versus flipping it in the same parity circuit, slide 7. |
| Cryptographic predictability from input combinations | The cubic received table agrees with an XOR of inputs on 7/8 of uniformly sampled inputs, slide 9. |
| Quantum error correction and single-qubit phase rotations | The toy gate and current paper's 48-qubit construction, slides 11–19. |

The 48-qubit code is a separate research construction using the same methods. Replacing each toy block by sixteen points alone does not specify its logical rows or prove its gate action.

## Revision decisions

- **Keep in the main talk:** ANF, first Boolean derivatives, complete majority decoding, Reed–Muller distance, input sensitivity, one Fourier score, the coding/cryptographic meaning of affine agreement, weights and intersections, complementary quantum codewords, the physical sign pattern, the current paper's signed-overlap criterion, and the qualified lower bound.
- **Keep in backup:** the detailed Fourier distance formula and complement rule, higher derivatives, degree/rate tables and the general distance proof, affine and extended-affine equivalence, full inclusion–exclusion, exact sign polynomial, and support classification details.
- **Omit from the delivered story:** the frontier-result tour, Mars photograph/application detour, sparse-spectrum testing, and separate cipher case studies. Earlier frontier research notes remain available. The adjacent applications now use the same parity and corrupted table, and require no new external research result.
- **Use proper TeX throughout:** conventional serif math fonts, operator names for weight and Reed–Muller codes, consistent binary addition, ordinary integer weights, and standard ket and quantum-code notation. Distinguish binary addition inside a function from integer arithmetic outside it.
- **Keep affine equivalence in backup.** A one-sentence observation about relabeling the cube is enough in the main talk. Promote the first affine slide only if symmetry/classification becomes a central topic, replacing about two minutes elsewhere rather than extending the talk.

The broader context remains concrete: ANF is an AND/XOR description of a computation; derivatives compare circuit outputs under input toggles; degree restrictions produce a communication code; spectral agreement identifies a recoverable message or an unwanted affine predictor; physical phases turn counts into a quantum operation. Claims that Boolean functions are broadly neglected, or that this toy example demonstrates a full cipher attack, are unnecessary.

## Main slides and timing

Numbers below are the visible main-slide numbers; the title is unnumbered.

| Slide | Minutes | Purpose |
| --- | ---: | --- |
| Title | 0.5 | Promise one story about recovery, prediction, and a quantum gate; preview three chapters. |
| 1. A damaged message can still contain an exact rule | 2 | Pose the recovery problem on an unmarked corrupted cube. |
| 2. A Boolean function becomes a transmitted word | 1.5 | Define the domain, table, binary addition, weight, and distance using entries. |
| 3. ANF turns a truth table into a polynomial | 3 | Expand the error indicator; distinguish algebraic degree from Hamming distance. |
| 4. Boolean derivatives turn edges into consistency checks | 2.5 | Compare endpoints; one bad entry spoils one of four disjoint checks. |
| 5. Local votes recover all four message bits | 3 | Recover three linear coefficients and then the constant. |
| 6. Affine rules split binary space into equal halves | 2.5 | Count the parity hyperplane, then derive distance four/eight and name RM(1,3). |
| 7. Changing one input can change every output | 3 | Distinguish observation from intervention in the clean parity circuit. |
| 8. Fourier analysis counts agreement with simple rules | 3 | Count agreements minus disagreements for the same received table. |
| 9. A useful decoder can reveal an unwanted predictor | 2.5 | Interpret 7/8 agreement in communication and cryptographic design. |
| 10. From recognizing a pattern to engineering an operation | 2.5 | Count faces, edges, and their intersections; begin the gate-design chapter. |
| 11. A quantum phase is a function of a binary word | 2 | Introduce relative phase, T, and the desired logical CCZ. |
| 12. Complementary codewords encode three quantum bits | 2 | Pair affine words; emphasize equal phase within an encoded pair. |
| 13. Parity chooses where to reverse the physical rotation | 1.5 | Return to the cube as the T/T-dagger placement pattern. |
| 14. The gate check is another Hamming-distance calculation | 2 | Calculate signed weight from distance to parity. |
| 15. A working gate still needs protection against phase errors | 1.5 | Distinguish distance two from three; motivate nonzero distinct columns. |
| 16. The 48-site geometry gives divisible codewords | 2 | Derive stabilizer weights 24 and 32 as whole-space weight minus deleted-subspace weight. |
| 17. Boolean label functions and signs complete the code | 2 | Show the paper's actual gate placement and code parameters. |
| 18. The paper reduces phase correctness to row overlaps | 3 | State the exact mod-8, mod-4, mod-2 conditions. |
| 19. Boolean structure also limits how short a code can be | 1.5 | Connect polynomial restrictions, geometric reductions, and logical-label tests; state the qualified bound. |
| 20. What the Boolean viewpoint made possible | 1.5 | Leave the construction, exact test, and lower bound visible during questions. |
| **Total** | **45** | **26 minutes through slide 10; 43.5 minutes through slide 19.** |

## Speaker guidance and exact calculations

Opening promise:

> By the end of this talk, you will follow one counting argument from repairing a corrupted message to controlling a quantum gate—and see why the same predictable structure matters in cryptography.

Use the title's three-part roadmap: recover a message, understand a rule, control a gate. Reach slide 6 by 15:00, slide 9 by 23:30, slide 10 by 26:00, slide 19 by 43:30, and the contributions by 45:00.

### Reveal and pause schedule

Only slides 5, 6, 14, and 18 have overlays. Concealed content reserves its final space, so diagrams and equations stay in position.

| Main slide | States | Delivery within the existing time |
| --- | ---: | --- |
| 5 | 2 | Show affine family and edge votes; ask “Why is this majority reliable?” Wait roughly seven seconds, then reveal all recovered coefficients and the constant. |
| 6 | 2 | Identify the four parity-one vertices first; then reveal the distance argument and code parameters. |
| 14 | 2 | Show signed weights without phases; ask “Do +4 and −4 give different phases when each count contributes an angle of π/4?” Wait roughly seven seconds, then reveal equal phases and logical CCZ. |
| 18 | 3 | Explain individual rows, then pairs, then triples at fixed positions. Reveal the logical-triple conclusion last. |

### Slides 1–3: distinguish message, input, and table

The sender's four message bits are the coefficients of

\[
f_{a,b}(u)=b+a_1u_1+a_2u_2+a_3u_3,\qquad u\in\mathbb F_2^3.
\]

The three-bit vector \(u\) indexes a transmitted position; the whole truth table is the eight-bit codeword. The worked message is \(a=111,b=0\), with parity table \(01101001\) in lexicographic order. The channel changes the entry at \(000\). The decoder is not told that location.

Introduce ANF as an exact AND/XOR polynomial, with \(u_i^2=u_i\) on binary inputs. The received polynomial is

\[
r=p+\delta_{000}
=1+u_1u_2+u_1u_3+u_2u_3+u_1u_2u_3.
\]

The high degree identifies departure from the allowed family, but degree alone does not measure the number of corrupted entries. Avoid a second cryptographic story here.

### Slides 4–6: let the audience perform the decoder

The derivative \(D_{e_i}f(u)=f(u+e_i)+f(u)\) compares two outputs. For an affine function the derivative is the constant \(a_i\). The four disjoint edges in direction \(e_1\) give votes \(0,1,1,1\). Majority recovers \(a_1=1\); the other directions recover \(a_2=a_3=1\). Removing the recovered parity leaves seven zeros and one one, so majority recovers \(b=0\).

The derivation uses the one-error promise and disjointness of the checks. A derivative responds to changing the input of a rule; a channel error changes one entry in its transmitted table. The decoder deliberately relates those two operations, but they are not identical noise models.

Describe the derivative as testing whether moving along an edge changes the output. On slide 5's first state, keep recovered coefficients concealed while the audience explains reliability: one corrupted endpoint affects only one of the four disjoint edge votes in a given direction. The second state completes all four message coefficients.

On slide 6, return to the clean parity coloring and identify each of the four points

\[
H=\{u:p(u)=1\}=\{100,010,001,111\}.
\]

A level set of a nonconstant affine Boolean function is an affine hyperplane. The picture marks four vertices; do not draw a Euclidean plane through those vertices. Pairing \(u\) with \(u+e_i\) for a nonzero coefficient proves that every such rule has four ones and four zeros. On the second reveal, apply this count to the difference of two distinct affine rules: a nonconstant difference has weight four; the constant-one difference has weight eight. Name the resulting [8,4,4] code only after explaining eight transmitted values, four message coefficients, and minimum distance four.

Keep the triangle-inequality proof oral: if both \(f\) and \(g\) were within distance one of \(r\), then \(d(f,g)\le d(f,r)+d(r,g)\le2\), contradicting distance at least four. Close the chapter with: “The decoder succeeds because the allowed rules cannot differ in only one or two places.”

### Slides 7–9: understand the same Boolean rule

Open the second chapter with: “The message is recovered. Now consider the same table as a computation: what changes its output, and what predicts it?” Return explicitly to the clean parity before discussing sensitivity. Under uniform inputs, knowing any one coordinate leaves parity equally likely to be zero or one. Flipping that coordinate changes every output. A derivative tests whether a displacement stays in the same output class or crosses to the other. Keep input observation, input intervention, and channel corruption distinct.

For the Fourier slide, the coefficient vector \(a\) selects an XOR of inputs, exactly as in the affine-message definition. The score

\[
W_f(a)=\sum_u(-1)^{f(u)+a\cdot u}
\]

uses real signs and ordinary integer addition. Each coefficient compares the table to the binary partition of an affine rule: agreements contribute +1 and disagreements −1. The displayed scores use zero-constant rules; complementing a rule reverses its score. For \(r\), the score is 6 at \(a=111\) and −2 elsewhere. The normalized Fourier coefficient of the sign function is \(W_f(a)/8\); basis, inversion, and Parseval material stay outside the main talk. Explain the plot as eight comparisons, with seven votes for the original parity surviving the one bad entry. Absolute values and the full affine-complement formula remain in backup.

Slide 9 interprets the same calculation in two settings. Coding deliberately restricts messages to a family whose structure enables recovery. A cryptographic Boolean component should resist accurate approximation by an affine combination of its inputs. The received table already has maximal ANF degree on three bits, yet parity predicts it with probability 7/8 under uniform input. High degree and low affine predictability are therefore distinct requirements. The small unbalanced example is not a proposed cryptographic component or a complete cipher attack. No cipher specification, new cryptographic notation, or additional example is needed.

### Slide 10: turn the analysis into a design question

Open the third chapter with: “Agreement helped the receiver and exposed a predictable output. Now we will choose Boolean patterns so that their counts produce a desired quantum operation.” The coordinate hyperplanes \(u_1=1\), \(u_2=1\), and \(u_3=1\) are faces of the cube. Products select their intersections: four points on a face, two on an edge, and one at the common vertex. Point to the two colored faces and the dark common edge when deriving

\[
\operatorname{wt}(f+g)=\operatorname{wt}(f)+\operatorname{wt}(g)-2\operatorname{wt}(fg).
\]

The overlap must be subtracted twice because XOR makes double-one positions zero. The table's weights 4, 2, 1 prepare the divisibility conditions. The full three-function identity and the general monomial weight \(2^{m-j}\) are speaker/backup details. The degree/rate table has moved to backup to make room for the advertised adjacent applications while keeping the total time fixed.

### Slides 11–14: finish the toy gate calculation

Introduce a relative sign through interference before asking the audience to read kets. A computational basis word records one bit per physical qubit. The phase from applying T independently is \(\omega^{\operatorname{wt}(v)}\), where \(\omega=e^{i\pi/4}\). CCZ changes the sign of logical label 111 alone.

The quantum encoding uses the eight disjoint pairs \(\{f_{a,0},f_{a,1}\}\). Equal amplitudes within each pair give an encoded basis state. Explain that all words in one encoded superposition must receive the same phase; checking only one representative would be insufficient.

Place T at parity-zero sites and its inverse at parity-one sites. The exact identity

\[
\operatorname{sw}_p(v)=\operatorname{wt}(p+v)-4
\]

reuses the distance calculation. For \(a\ne111\), both complements give signed weight zero. For \(a=111\), the two values are −4 and +4. Pause with those counts visible and the phase column concealed; use the question in the reveal schedule. Both counts give phase −1. The calculation proves the gate on every encoded basis state and hence on every encoded superposition by linearity. The main Fourier slide has already explained agreement counts, but the gate proof still uses the direct integer identity rather than a spectral theorem.

### Slides 15–18: explain what the paper adds

The toy code has \(d_X=4,d_Z=2\), so quantum distance two. Define CSS briefly as separate binary constraints for bit and phase errors. A column lists how a physical phase error responds to the X-type stabilizer checks. Nonzero, distinct columns exclude undetected phase errors of weights one and two. The projectivity condition is sufficient for this protection; avoid calling it necessary for every CSS code.

The paper retains \((u,w)\in\mathbb F_2^4\times\mathbb F_2^2\) with \(w\ne0\): whole space minus the four-dimensional subspace \(w=0\). Every nonzero linear rule \(\ell(u,w)=\alpha\cdot u+\beta\cdot w\) has 32 ones on the full six-dimensional space. On the deleted subspace, the restriction is \(\alpha\cdot u\): eight ones if \(\alpha\ne0\), zero if \(\alpha=0\). Subtraction gives 24 and 32 respectively; the second nonzero case requires \(\beta\ne0\). The zero rule is implicit in the slide's nonzero cases and has weight zero. Close with: “The half-space count that explained our classical distance now gives stabilizer weights divisible by eight.” Eight-divisibility is a feature of this construction, stronger than the parity conditions needed in the wider lower-bound class.

Use slide 17's three steps: **choose physical sites → assign logical labels → choose rotation signs.** The sites determine the stabilizer evaluation geometry. The six stabilizer rows generate the words added within an encoded superposition; three independent logical Boolean functions distinguish the eight encoded basis states. The sign function chooses T or T-dagger at each physical site. Geometry alone does not specify the completed code. The actual gate diagram evaluates the paper's sign function, giving 6, 6, and 10 inverse rotations in the three blocks. Keep the full logical-label table in the paper/tutorials and the sign polynomial in backup. The code has \(d_X=16,d_Z=3\).

In the overlap criterion, products mean coordinatewise intersections. Reveal individual rows first (coefficient 1), pairs second (coefficient −2), and triples third (coefficient 4), recalling slide 10's pair identity. Keep every equation in its final position throughout the three states. Single-row and pair terms vanish modulo eight after their coefficients are applied; only the three-logical-row intersection contributes the required cubic phase. All triples involving a stabilizer row must contribute zero. Terms involving four or more rows have coefficients divisible by eight and disappear. The full formula remains available in backup.

### Slides 19–20: preserve the scope of the result

Follow slide 19's progression: **polynomial restrictions → geometric reductions → logical-label tests.** Explain orally that a polynomial factor can confine a support to a hyperplane, enabling a reduction under the paper's hypotheses. The full example and origin cases belong in backup. A support restriction alone does not establish the existence or impossibility of a completed quantum code; the logical-label tests remain necessary.

The exclusion is for CSS codes with three logical qubits, \(d_Z\ge3\), and the nine Campbell–Howard conditions. Those conditions permit a diagonal Clifford correction after physical T gates. The native construction implements the desired gate with its chosen T/T-dagger pattern without a further logical correction. The two statements concern different allowed implementations.

The lower bound rules out lengths at most 38, at any stabilizer rank. Lengths 39–46 remain open in that class. The paper's particular 47-qubit example lacks a native sign pattern; that fact does not rule out every 47-qubit code. Avoid a global-minimality claim for the 48-qubit construction.

Leave slide 20 visible throughout general questions. Repeat the opening connection: the same Boolean structure supports recovery, exposes predictability, and can be chosen to produce an encoded phase. Return to an appropriate backup only when a question needs it.

## Backup order and affine-equivalence decision

1. **Input-affine equivalence:** \(g(u)=f(Au+t)\); position permutation preserves weight, degree, and pairwise distance under the same substitution; \(D_vg(u)=D_{Av}f(Au+t)\).
2. **The same corrupted cube after translation:** \(t=100\) gives \(r(u+t)=p(u)+1+\delta_t(u)\). Relabeling transports the decoding argument and removes duplicate cases in searches.
3. **Extended-affine convention and puncturing:** adding an affine output function preserves distance to the affine family but can change weight. A distinguished deleted origin requires care under translations.
4. **A translated hyperplane can change syndrome rank:** the four-point faces at z=1 and z=0 both have affine dimension two but column ranks three and two. Translating syndrome entries differs from permuting physical positions while transporting all code data. Zero syndrome need not mean a zero full generator column; the example is not a QEC-equivalence claim.
5. **A polynomial factor exposes a geometric reduction:** \(c=y_8(g+y_7h)\) confines the support to \(y_8=1\). After choosing the origin, a containing hyperplane through zero bounds actual rank by seven. An origin-avoiding rank-eight support is proper because \(n\le38<128\); a missing point supplies a projection direction under the paper's CH, k=3, dZ≥3, and distinct-nonzero-syndrome hypotheses. Keep the full-support puncturing derivation in the tutorials.
6. **Higher derivatives:** recover ANF coefficients at zero; the third derivative is the parity check of RM(2,3).
7. **Reed–Muller distance:** short induction and general parameters.
8. **Degree and rate:** the four RM(d,3) parameter sets and their error guarantees.
9. **Detailed Fourier decoder:** correlations give nearest-affine distance, and score signs account for complements.
10. **Full overlap identity:** inclusion–exclusion, signed counts, and disappearance of four-way terms modulo eight.
11. **Toy quantum distance:** distinguish the primal and dual constraints.
12. **Full signed-weight test:** all logical and stabilizer labels, plus the block-weight identity.
13. **48-qubit sign polynomial:** precise formula and diagram coordinate convention.
14. **Length bounds and support restrictions:** qualified status table, punctured Reed–Muller support, and spanning condition.
15. **Essential sources:** the current manuscript first; classical texts for fundamentals.

Affine equivalence is most useful for questions about symmetry, classification, or why alternate formulas represent the same object. The main argument needs neither its matrix notation nor the output-affine convention. Keep the first backup for questions; promoting it would require replacing another main topic and weakening the match to the abstract.

The affine-hyperplane walkthrough supplies the new geometric explanations; the weight/degree and sign-pattern notes reinforce counting and the distinction between sites, labels, and signs. Check the hypotheses against the active paper before using a tutorial reduction. Classification tables, quadratic polar matrices, orbit enumeration, and first-principles sign-pattern derivations remain in the tutorials.

## Rehearsal acceptance still requiring a listener

Rehearse with a mathematically mature listener outside QEC. Ask the listener to explain why a nonconstant affine rule gives a hyperplane of weight four, why deleting a subspace gives weights 24 and 32, and why both words in an encoded pair need the same phase. Time the five completion points above, including both seven-second pauses. Compilation, finite checks, and page inspection establish artifact correctness; the listener establishes whether the explanation and 45-minute budget fit the audience.

## Source grounding and verification

The research slides were checked against the active manuscript sections: the introduction and FG48 construction; the fixed logical-label table, signed-overlap and block criteria, and explicit sign-pattern proposition; the minimality section; and the conclusion. Commented or disabled superseded passages were not treated as the current result.

The external background is restricted to elementary results used explicitly in the calculations: MacWilliams–Sloane and Huffman–Pless for Reed–Muller coding; Carlet for ANF, derivatives, affine predictability, and equivalence; O'Donnell for the Walsh viewpoint. No new frontier-result or historical-application claim is made in the revised main deck. The main spectrum and the 7/8 prediction statement are direct calculations on the recurring example.

The Fourier agreement interpretation is stated in O'Donnell's [Propositions 1.8–1.9](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf#page=25). Carlet's [section on nonlinearity, pp. 50–51](https://www.math.univ-paris13.fr/~carlet/chap-fcts-Bool-corr.pdf#page=50), explains why distance from affine functions matters for cryptographic Boolean components. The main slides use only this basic design connection, not a security conclusion about a specific cipher.

Independent finite checks passed for all 144 affine-message/no-error-or-single-error cases; all four RM(d,3) dimensions and distances; all 16 toy phase calculations; and affine degree, weight, and derivative transport on all 256 three-variable truth tables for an invertible shear and translation. For the current 48-qubit data, checks reproduced ranks 6 and 9, stabilizer weight counts, the 26/22 sign count, all 129 single/pair/triple congruences, and all 512 encoded-word phase conditions. Exhaustive logical-X enumeration gives distance 16; distinct nonzero syndrome columns and a weight-three logical-Z witness give distance 3. These checks validate the finite examples, not the paper's general lower-bound proof.

The hyperplane revision additionally checks all 120 distinct pairs of affine codewords, all 63 nonzero six-variable linear rules using whole-space and deleted-subspace counts separately, and the backup's column ranks three/two and affine dimensions two/two. The rebuilt PDF has 41 pages, 20 numbered main slides, and 15 backups; exactly slides 5, 6, 14, and 18 have overlays. Character-position comparisons across all five reveal transitions confirm stable placement, and page inspection checks the diagrams and concealed answers. Compilation reports no overflow or missing glyphs. The timing table totals 45 minutes, including 26 minutes through slide 10; the title and abstract are preserved. The listener rehearsal remains pending.

Winston-specific delivery proposals, sources, and the distinction between implemented changes and rehearsal suggestions are in [the speaking notes](speaking_notes.md).
